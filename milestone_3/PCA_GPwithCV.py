# -*- coding: utf-8 -*-
"""

@author: Carter
"""

import numpy as np

from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF, Matern
from sklearn.model_selection import KFold
from sklearn.decomposition import PCA

#trains a GP classifier and returns the predictions for Xgp_test data
def runGP(kernel, Xgp_train, ygp_train, Xgp_test):
    gp = GaussianProcessClassifier(kernel=kernel).fit(Xgp_train,ygp_train)
    ygp_preds = gp.predict(Xgp_test)
    return ygp_preds 

#import data & combine
gKeyData = np.genfromtxt('gKeyData.csv', delimiter=',')
dKeyData = np.genfromtxt('dKeyData.csv', delimiter=',')
fullDataset = np.concatenate((dKeyData, gKeyData), axis=1)
fullDataset = np.transpose(fullDataset)

#randomize the dataset order
np.random.shuffle(fullDataset)
fullDataset = np.transpose(fullDataset)

X_full = fullDataset[:12,:]
y_full = fullDataset[12, :]

def getPCAreduce(X_trainPCA, X_testPCA, svd_bool):
    if (svd_bool == 0):
        pca = PCA(n_components = 'mle', svd_solver='full')
        pca.fit(X_trainPCA.T)
    else:
        pca = PCA(n_components = 9)
        pca.fit(X_trainPCA.T)
        
    newTrain =  pca.transform(X_trainPCA.T)
    newTest = pca.transform(X_testPCA.T)
    return newTrain, newTest
    
    
    
    
#runs 'numFolds'-fold cross validation on GP classification with kernel k_CV
def runCVonGP(numFolds, X, y, k_CV, PCA_bool): 
    avErrVec = np.zeros(numFolds);
    #numSamples = len(X[0])
    
    kf = KFold(n_splits=numFolds)
    
    X= X.T
    y= y.T
    
    foldNum=0
    for train_index, test_index in kf.split(X):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
        
        X_train = X_train.T
        X_test = X_test.T
        
        if(PCA_bool == 1):
            [X_train, X_test] = getPCAreduce(X_train, X_test, 0)
            print(X_train.shape)
        elif(PCA_bool == 2):
            [X_train, X_test] = getPCAreduce(X_train, X_test, 1)
            print(X_train.shape)
        else:
            X_train = X_train.T
            X_test = X_test.T

        
        #train GP classifier and get predictions of test set
        y_preds = runGP(k_CV, X_train, y_train, X_test)
        
        #calculate %error
        numWrong = 0;
        for h in range(len(y_preds)):
            if(y_preds[h] != y_test[h]):
                numWrong = numWrong +1   
            #print("prediction: ", y_preds[h], " label: ", y_test[h])
            
        percError = (numWrong/len(y_preds))*100
        
        
        avErrVec[foldNum] = percError
        foldNum = foldNum +1
        
    averageError = sum(avErrVec)/numFolds
    return averageError


totalErrNoPCA = runCVonGP(10, X_full, y_full, 1.0 * RBF([1.0]), 0)
print("without PCA")
print("Average Percent Error:", round(totalErrNoPCA, 4), "%")

totalErrWithPCAandSVD = runCVonGP(10, X_full, y_full, 1.0 * RBF([1.0]), 1)
print("\nwith auto PCA/SVD")
print("Average Percent Error:", round(totalErrWithPCAandSVD, 4), "%")

totalErrWithPCA = runCVonGP(10, X_full, y_full, 1.0 * RBF([1.0]), 2)
print("\nwith PCA/SVD forced to 9")
print("Average Percent Error:", round(totalErrWithPCA, 4), "%")



    
    
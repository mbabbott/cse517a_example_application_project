# -*- coding: utf-8 -*-
"""

@author: Carter
"""

import numpy as np

from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF, Matern
from sklearn.model_selection import KFold

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

#runs 'numFolds'-fold cross validation on GP classification with kernel k_CV
def runCVonGP(numFolds, X, y, k_CV): 
    avErrVec = np.zeros(numFolds);
    #numSamples = len(X[0])
    
    kf = KFold(n_splits=numFolds)
    
    X= X.T
    y= y.T
    
    foldNum=0
    for train_index, test_index in kf.split(X):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]

        #train GP classifier and get predictions of test set
        y_preds = runGP(k_CV, X_train, y_train, X_test)
        
        #calculate %error
        numWrong = 0;
        for h in range(len(y_preds)):
            if(y_preds[h] != y_test[h]):
                numWrong = numWrong +1   
            #print("prediction: ", y_preds[h], " label: ", y_test[h])
            
        percError = (numWrong/len(y_preds))*100
        
        #print("Fold #:", foldNum)
        #print("Percent Error", round(percError, 2),"%")
        
        avErrVec[foldNum] = percError
        foldNum = foldNum +1
        
    averageError = sum(avErrVec)/numFolds
    return averageError

totalErr1 = runCVonGP(10, X_full, y_full, 1.0 * RBF([1.0]))
print("\nAverage Percent Error:", round(totalErr1, 2), "%")
print("Kernel: RBF(1)\n")

totalErr4 = runCVonGP(10, X_full, y_full, Matern(length_scale=1))
print("\nAverage Percent Error:", round(totalErr4, 2), "%")
print("Kernel: Matern(1)\n")

totalErr2 = runCVonGP(10, X_full, y_full, 1.0 * RBF([10.0]))
print("\nAverage Percent Error:", round(totalErr2, 2), "%")
print("Kernel: RBF(10)\n")

totalErr5 = runCVonGP(10, X_full, y_full, Matern(length_scale=10))
print("\nAverage Percent Error:", round(totalErr5, 2), "%")
print("Kernel: Matern(10)\n")

totalErr3 = runCVonGP(10, X_full, y_full, 1.0 * RBF([100.0]))
print("\nAverage Percent Error:", round(totalErr3, 2), "%")
print("Kernel: RBF(100)\n")

totalErr6 = runCVonGP(10, X_full, y_full, Matern(length_scale=100))
print("\nAverage Percent Error:", round(totalErr6, 2), "%")
print("Kernel: Matern(100)\n")
    
    
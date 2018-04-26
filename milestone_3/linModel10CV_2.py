# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 01:56:14 2018

@author: Carter
"""

import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error

#fullDataset = np.genfromtxt('bachDatasetWithLabels.csv', delimiter=',')
gKeyData = np.genfromtxt('gKeyData.csv', delimiter=',')
dKeyData = np.genfromtxt('dKeyData.csv', delimiter=',')

fullDataset = np.concatenate((dKeyData, gKeyData), axis=1)

fullDataset = np.transpose(fullDataset)
np.random.shuffle(fullDataset)

fullDataset = np.transpose(fullDataset)



X = fullDataset[:12,:]
y = fullDataset[12, :]

#set the training data to literally be the label
#for i in range(0,12):
 #   X[i,:] = y


numSamples = len(X[0])
splitCol = int(numSamples*.66)

#for k in range(len(y)):
#    if (y[k] == 14):
#        y[k] = 1
#        
#    else:
#        y[k] = 0

X_train = X[:, :splitCol]
#X_train = X_train.reshape((splitCol,12))
X_train = X_train.T
y_train = y[:splitCol]
#y_train = y_train.reshape((splitCol, 1))

X_test = X[:, splitCol:]
#X_test = X_test.reshape((numSamples-splitCol,12))
X_test = X_test.T
y_test = y[splitCol:]
#y_test = y_test.reshape((numSamples-splitCol,1))



logModel = linear_model.LogisticRegressionCV(cv=10)
#logModel = linear_model.LinearRegression()
logModel.fit(X_train, y_train)

y_preds = logModel.predict(X_test)

for h in range(len(y_preds)):
    print("prediction: ", y_preds[h], " label: ", y_test[h])
    

print("Mean squared error: %.2f" % mean_squared_error(y_test, y_preds))
# -*- coding: utf-8 -*-
"""

@author: Carter
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

def getPCAreduce(X):
    
    pca = PCA(n_components = 9)
    pca.fit(X.T)
    return pca.transform(X.T)
    
def plot(x1, x2, classlbl):
    if (classlbl == 0):
        plt.scatter(x1, x2, c='b')
    if (classlbl == 1):
        plt.scatter(x1, x2, c='r')
    return
    
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

X_2D = TSNE(n_components=2).fit_transform(np.copy(X_full.T))

plt.figure(0)
for i in range(0, X_2D.shape[0]):
    label= y_full[i]
    plot(X_2D[i][0], X_2D[i][1], label)
plt.show()

X_PCA = getPCAreduce(np.copy(X_full))
X_PCA_2D = TSNE(n_components=2).fit_transform(np.copy(X_PCA))

plt.figure(0)
for i in range(0, X_2D.shape[0]):
    label= y_full[i]
    plot(X_PCA_2D[i][0], X_PCA_2D[i][1], label)
    
plt.show()


 
    
    
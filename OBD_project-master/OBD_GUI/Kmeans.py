
'''

@author: Daben

@contact: dabenw@uci.edu

@file: Kmeans.py

@time: 2019/4/19

@desc: k-means cluster

'''

from numpy import *
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import xlrd
import numpy as np
import pandas as pd


# data=[[0.404120557,0,1,0,0],
#       [0.512964448,0,1,0,0],
#       [0.496052632,0,1,0,0],
#       [0.376337948,0.301478953,0.481481481,0.185185185,0.333333333],
#       [0.659807956,0.408969409,0.393939394,0.151515152,0.454545455],
#       [0.355084799,0.169566761,0.608695652,0.239130435,0.152173913],
#       [0.417582103,0.043360914,0.862745098,0.098039216,0.039215686],
#       [0.485730362,0.072690972,0.848484848,0.060606061,0.090909091],
#       [0.540712152,0,0.933333333,0.066666667,0],
#       [0.386690602,0,1,0,0]]
Data=[]
data = xlrd.open_workbook('KMeansData.xlsx')
table = data.sheet_by_index(0)
for i in range(0,table.nrows):
    Data.append(table.row_values(i))
Data = np.array(Data)
Data = Data.astype(np.float64)

print(Data)


km_cluster = KMeans(n_clusters=3, max_iter=300, n_init=40, init='k-means++',n_jobs=-1)
km_cluster.fit(Data)
labels = km_cluster.labels_
cluster0 =Data[(km_cluster.labels_==0)]
cluster1 =Data[(km_cluster.labels_==1)]
cluster2 =Data[(km_cluster.labels_==2)]
# cluster3 =Data[(km_cluster.labels_==3)]
print(labels)
print("-----")
centers = km_cluster.cluster_centers_
print(centers)
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(cluster0[:,1],cluster0[:,2],cluster0[:,3],c='r',label='first cluster')
ax.scatter(cluster1[:,1],cluster1[:,2],cluster1[:,3],c='b',label='second cluster')
ax.scatter(cluster2[:,1],cluster2[:,2],cluster2[:,3],c='g',label='third cluster')
# ax.scatter(cluster3[:,1],cluster3[:,2],cluster3[:,3],c='y',label='fourth cluster')

ax.scatter(centers[0][1],centers[0][2],centers[0][3],marker='*',c='r')
ax.scatter(centers[1][1],centers[1][2],centers[1][3],marker='1',c='b')
ax.scatter(centers[2][1],centers[2][2],centers[2][3],marker='P',c='g')
# ax.scatter(centers[3][1],centers[3][2],centers[3][3],marker='x',c='y')

ax.legend(loc='best')

ax.set_zlabel('high num', fontdict={'size': 15, 'color': 'red'})
ax.set_ylabel('medium num', fontdict={'size': 15, 'color': 'red'})
ax.set_xlabel('normal num', fontdict={'size': 15, 'color': 'red'})

plt.show()




# this is the elbow method
SSE = []  # sum of the squared errors
# num_clusters = 2
for num_clusters in range(1,6):
    km_cluster = KMeans(n_clusters=num_clusters, max_iter=300, n_init=40, init='k-means++',n_jobs=-1)
    km_cluster.fit(Data)
    SSE.append(km_cluster.inertia_)
X = range(1,6)
plt.xlabel('k')
plt.ylabel('SSE')
plt.plot(X,SSE,'o-')
plt.show()
# labels = km_cluster.labels_
center = km_cluster.cluster_centers_
# predict = km_cluster.predict(data)
# print(labels)
# print(center)
# print(predict)




# this is the Average silhouette method
Scores = []
for num_clusters in range(2,6):
    km_cluster = KMeans(n_clusters=num_clusters, max_iter=300, n_init=40, init='k-means++', n_jobs=-1)
    km_cluster.fit(Data)
    Scores.append(silhouette_score(Data,km_cluster.labels_,metric='euclidean'))
X = range(2,6)
plt.xlabel('k')
plt.ylabel('average silhouette width ')
plt.plot(X,Scores,'o-')
plt.show()

# writing our own Knn based on euclidean distance
from math import sqrt
import numpy as np 
import warnings  # to warn user when writing numbers
# import matplotlib.pyplot as plt
# from matplotlib import style
from collections import Counter
import pandas as pd
import random

# style.use("fivethirtyeight")

# Intro to 2D euclidean distance
# plot1 = [1,3]
# plot2 = [2,5]
# euclidean distance 
# euclidean_distance = sqrt((plot1[0]-plot2[0])**2+(plot1[1]-plot2[1])**2)
# print(euclidean_distance)

# simple dataset for testing before applying to other datasets
# dataset = {'k':[[1,2],[2,3],[3,1]],'r':[[6,5],[7,7],[8,6]]}
# new_feature = [5,7]

# for i in dataset:
#     for j in dataset[i]:
#         plt.scatter(j[0],j[1], s=100, color=i)
# [[plt.scatter(j[0],j[1],s=100,color=i) for j in dataset[i]] for i in dataset]
# plt.scatter(new_feature[0],new_feature[1],s=200,color='g')
# plt.show()

def k_nearest_neighbors(data, predict, k=3):
    if len(data) >= k:
        warnings.warn("K is set to a value less that total voting groups!!")
        
    # knn_algorithm
    distances = []
    for group in data:
        for features in data[group]:
            # euclidean_distance = np.sqrt(np.sum((np.array(features)-np.array(predict))**2))
            euclidean_distance = np.linalg.norm(np.array(features)-np.array(predict))
            distances.append([euclidean_distance,group])

    votes = [i[1] for i in sorted(distances) [:k]]
    # print(Counter(votes).most_common(1))
    vote_result = Counter(votes).most_common(1)[0][0]
    confidence = Counter(votes).most_common(1)[0][1] / k
    return vote_result, confidence

# result = k_nearest_neighbors(dataset, new_feature, k=3)
# print(result)

# [[plt.scatter(j[0],j[1],s=100,color=i) for j in dataset[i]] for i in dataset]
# plt.scatter(new_feature[0],new_feature[1],s=200,color=result)
# plt.show()

# to try with real data and compare with scikit results
df = pd.read_csv("MachineLearning/Data/breast-cancer-wisconsin.data")
df.replace('?', -99999, inplace=True)
df.drop(["id"],1,inplace=True)
full_data = df.astype(float).values.tolist() # make sure that data is float values

random.shuffle(full_data)
test_size = 0.2
train_set = {2:[], 4:[]}
test_set = {2:[], 4:[]}
train_data = full_data[:-int(test_size*len(full_data))]
test_data = full_data[-int(test_size*len(full_data)):]

for i in train_data:
    train_set[i[-1]].append(i[:-1])

for i in test_data:
    test_set[i[-1]].append(i[:-1])

correct = 0
total = 0

for group in test_set:
    for data in test_set[group]:
        vote, confidence = k_nearest_neighbors(train_set, data, k=5)
        if group == vote:
            correct += 1
        else:
            confidence
        total += 1
print("Accuracy:", correct/total)
     
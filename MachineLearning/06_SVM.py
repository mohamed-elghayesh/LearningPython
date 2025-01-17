# an example that uses built-in neighbors.KNeighborsClassifier()
import numpy as np 
from sklearn import preprocessing, svm, model_selection
import pandas as pd 

df = pd.read_csv("MachineLearning/Data/breast-cancer-wisconsin.data")
df.replace("?", -99999,inplace=True)
df.drop(["id"], 1, inplace=True)

X = np.array(df.drop(["class"],1))
y = np.array(df["class"])

X_train, X_test, y_train, y_test = model_selection.train_test_split(X,y,test_size=0.2,random_state=42)

clf = svm.SVC()
clf.fit(X_train,y_train)

accuracy = clf.score(X_test, y_test)
print(accuracy)

# an example to predict
example_measures = np.array([[10,2,6,9,1,2,3,2,8],[4,2,5,5,1,2,3,2,6],[4,2,6,1,8,2,3,2,1]])
example_measures = example_measures.reshape(len(example_measures),-1)

prediction = clf.predict(example_measures)
print(prediction)

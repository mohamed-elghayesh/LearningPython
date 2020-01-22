# simple linear regression example on stock prices
import pandas as pd
import quandl, math, datetime
import numpy as np
from sklearn import preprocessing, model_selection, svm # model_selection replaces cross_validation in python 3
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt
from matplotlib import style
import pickle

style.use('ggplot') # to make the plot looks decent

# df = quandl.get('WIKI/GOOGL') # gets datasets from url, 3424 row x 12 col, daily records from year 2004 to 2018
# df.to_csv('MachineLearning/Data/stock.csv')
# print (df) # Open, High, Low, Close, Volume, Ex-Dividend, Split Ratio, Adj. Open, Adj. High, Adj. Low, Adj. Close, Adj. Volume

df = pd.read_csv('MachineLearning/Data/stock.csv')

df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']] # select only these columns
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0 # add new calculated column HL_PCT --> df (5 columns)
df['PCT_Change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0 # add another calculated column PCT_Change --> df (6 columns)

df = df[['Adj. Close','HL_PCT','PCT_Change','Adj. Volume']] # our new df, select columns --> df (4 columns)

forecast_col = 'Adj. Close' # will use Adj. Close to forcast
df.fillna(-999999999, inplace=True) # fill empty or nan values in df with -99999 to avoid nan errors

# take only 1% of the rows as forecast and remove them from the df
forecast_out = int(math.ceil(0.1*len(df))) # predict 10% of the dataframe values (number of days in future)
df['label'] = df[forecast_col].shift(-forecast_out) # add new column label, take its values from Adj. Close (-ve shifts-up top 35 rows), will put NaNs at the bottom 35 rows

# features X upper case, lables y lower case
X = np.array(df.drop(['label'],1)) # X now has df except (label) column
X = preprocessing.scale(X) # centers the values around the mean
X_lately = X[-forecast_out:] # X:df opposit to NaNs in label
X = X[:-forecast_out]

df.dropna(inplace=True) # remove the NaNs (the last 35 rows data), total number of rows decreased for all df including label
y = np.array(df['label']) # y now has the label

# linear regression steps / SVM steps
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)

# region pickling to avoid retraining
# clf = LinearRegression(n_jobs=-1) # train in parallel as many threads as possible (curve line fitting)
# clf = svm.SVR(kernel='poly')
# clf.fit(X_train, y_train)

# pickle or save the classifier after fitting to avoid training largr datasets each time
# with open('MachineLearning/Data/LinearRegression.pickle','wb') as f:
#     pickle.dump(clf, f)
# endregion
pickle_in = open('MachineLearning/Data/LinearRegression.pickle','rb')
clf = pickle.load(pickle_in)

accuracy = clf.score(X_test, y_test)

forecast_set = clf.predict(X_lately) # X_lately values are the most recent and have no y values, we will predict them now
print(forecast_set, accuracy, forecast_out)

# plotting the data and the prediction for Adj. Close
df['Forecast'] = np.nan
last_date = df.iloc[-1].name
dti = pd.date_range(last_date, periods=forecast_out+1, freq='D')
index = 1

for i in forecast_set:
    df.loc[dti[index]] = [np.nan for _ in range(len(df.columns)-1)] + [i]
    index +=1

df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4) # location of the legend
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()

# print(accuracy)
# print(df.head())
# print(df.tail())
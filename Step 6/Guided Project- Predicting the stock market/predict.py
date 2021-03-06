import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import statsmodels.api as sm
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

stocks = pd.read_csv('sphist.csv')

stocks['Date'] = pd.to_datetime(stocks['Date'])
#print(stocks.dtypes)

stocks = stocks.sort_values('Date', ascending=True)
stocks = stocks.reset_index()
# print(stocks.head())

plt.plot(stocks['Date'], stocks['Close'])
plt.show()

mean_5_days = pd.rolling_mean(stocks['Close'], window=5).shift(1)
stocks['mean_5_days'] = mean_5_days

mean_365_days = pd.rolling_mean(stocks['Close'], window=365).shift(1)
stocks['mean_365_days'] = mean_365_days

mean_ratio = mean_5_days / mean_365_days
stocks['mean_ratio'] = mean_ratio

std_5_days = pd.rolling_std(stocks['Close'], window=5).shift(1)
stocks['std_5_days'] = std_5_days

std_365_days = pd.rolling_std(stocks['Close'], window=365).shift(1)
stocks['std_365_days'] = std_365_days

std_ratio = std_5_days / std_365_days
stocks['std_ratio'] = std_ratio

volume_5_days = pd.rolling_mean(stocks['Volume'], window= 5).shift(1)
stocks['Volume_5_days'] = volume_5_days

volume_365_days = pd.rolling_mean(stocks['Volume'], window= 365).shift(1)
stocks['Volume_365_days'] = volume_365_days

volume_ratio = volume_5_days / volume_365_days
stocks['volume_ratio'] = volume_ratio

std_volume_5_days = pd.rolling_std(stocks['Volume'], window= 5).shift(1)
stocks['STD_Volume_5_days'] = std_volume_5_days

std_volume_365_days = pd.rolling_std(stocks['Volume'], window= 365).shift(1)
stocks['STD_Volume_365_days'] = std_volume_365_days

std_volume_ratio = std_volume_5_days / std_volume_365_days
stocks['std_volume_ratio'] = std_volume_ratio


# filtering the stocks(getting rid of NaN rows)
filtered_stocks = stocks[pd.notnull(stocks['mean_365_days'])]

train = filtered_stocks[filtered_stocks['Date'] < datetime(year=2013, month=1, day=1)]

test = filtered_stocks[filtered_stocks['Date'] >= datetime(year=2013, month=1, day=1)]

features = ['mean_5_days', 'mean_365_days', 'mean_ratio', 'std_5_days', 'std_365_days', 'std_ratio', 
			'Volume_5_days', 'Volume_365_days', 'volume_ratio', 'STD_Volume_5_days', 
			'STD_Volume_365_days', 'std_volume_ratio']

X_train = train[features]
Y_train = train['Close']

X_test = test[features]
Y_test = test['Close']

lr = LinearRegression()
lr.fit(X_train, Y_train)

predictions = lr.predict(X_test)
#print(predictions)
test['Predictions'] = predictions

mae = mean_absolute_error(Y_test, predictions)
mse = mean_squared_error(Y_test, predictions)
rmse = mse**(1/2)

r2 = r2_score(Y_test, predictions)

print(test)

print("Mean Absolute error: ",mae)
print("Mean Squared Error: ",mse)
print("Root Mean Squared Error: ",rmse)
print("R Squared: ",r2)

# # OLS method
# linear = sm.OLS(Y_train, X_train)
# linearfit = linear.fit()
# print(linearfit.summary())


## 1. Introduction to the data ##

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

hollywood_movies = pd.read_csv('hollywood_movies.csv')
#print(hollywood_movies.head())

#print(hollywood_movies['exclude'].value_counts())

# AXIS=1 INDICATES THAT WE ARE DROPPING A COLUMN
hollywood_movies = hollywood_movies.drop('exclude', axis=1)
print (hollywood_movies)


## 2. Scatter plots - profitability and audience ratings ##

fig = plt.figure(figsize=(6,10))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

ax1.scatter(hollywood_movies['Profitability'], hollywood_movies['Audience Rating'])
ax1.set_xlabel('Profitability')
ax1.set_ylabel('Audience Rating')
ax1.set_title('Hollywood Movies, 2007-2011')

ax2.scatter(hollywood_movies['Audience Rating'], hollywood_movies['Profitability'])
ax2.set_ylabel('Profitability')
ax2.set_xlabel('Audience Rating')
ax2.set_title('Hollywood Movies, 2007-2011')

plt.show()

## 3. Scatter matrix - profitability and critic ratings ##

normal_movies = hollywood_movies[hollywood_movies['Film'] != 'Paranormal Activity']
df = normal_movies[['Profitability','Audience Rating']]
scatter_matrix(df, figsize=(6,6))
plt.show()

## 4. Box plot - audience and critic ratings ##

df = normal_movies[['Critic Rating', 'Audience Rating']]
df.plot(kind='box')
plt.show()

## 5. Box plot - critic vs audience ratings per year ##

normal_movies = normal_movies.sort_values('Year')
fig = plt.figure(figsize=(8,4))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

sns.boxplot(x=normal_movies['Year'], y=normal_movies['Critic Rating'], ax=ax1)

sns.boxplot(x=normal_movies['Year'], y=normal_movies['Audience Rating'], ax=ax2)

plt.show()

## 6. Box plots - profitable vs unprofitable movies ##

def is_profitable(row):
    if row["Profitability"] <= 1.0:
        return False
    return True
normal_movies["Profitable"] = normal_movies.apply(is_profitable, axis=1)
print(normal_movies["Profitable"].value_counts())

fig = plt.figure(figsize=(12,6))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

sns.boxplot(x=normal_movies['Profitable'], y=normal_movies['Audience Rating'], ax=ax1)
sns.boxplot(x=normal_movies['Profitable'], y=normal_movies['Critic Rating'], ax=ax2)

plt.show()

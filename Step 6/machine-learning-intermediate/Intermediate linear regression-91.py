## 1. Introduction to the Data ##

import pandas
import matplotlib.pyplot as plt
%matplotlib inline

pisa = pandas.DataFrame({"year": range(1975, 1988), 
                         "lean": [2.9642, 2.9644, 2.9656, 2.9667, 2.9673, 2.9688, 2.9696, 
                                  2.9698, 2.9713, 2.9717, 2.9725, 2.9742, 2.9757]})

print(pisa)

pisa.plot('year', 'lean', kind='scatter')

## 2. Fit the Linear Model ##

import statsmodels.api as sm

y = pisa.lean # target
X = pisa.year  # features
X = sm.add_constant(X)  # add a column of 1's as the constant term

# OLS -- Ordinary Least Squares Fit
linear = sm.OLS(y, X)
# fit model
linearfit = linear.fit()
print(linearfit.summary())

## 3. Define a Basic Linear Model ##

# Our predicted values of y
yhat = linearfit.predict(X)
print(yhat)

residuals = yhat - y

## 4. Histogram of Residuals ##

# The variable residuals is in memory
plt.hist(residuals, bins=5)
plt.show()

## 6. Sum of Squares ##

import numpy as np

# sum the (predicted - observed) squared
SSE = np.sum((yhat-y.values)**2)
yi_mean = np.mean(y) 
RSS = np.sum((yi_mean - yhat) ** 2)
TSS = np.sum((y.values - yi_mean) ** 2)
print(SSE, RSS, TSS)

## 7. R-Squared ##

# Variables SSE, RSS, and TSS are in memory
R2 = RSS / TSS
print(R2)

## 9. Coefficients of the Linear Model ##

# Print the models summary
#print(linearfit.summary())

#The models parameters
print("\n",linearfit.params)
delta = 15 * linearfit.params['year'] 

## 10. Variance of Coefficients ##

# Enter your code here.
# Compute SSE
SSE = np.sum((y.values - yhat)**2)
# Compute variance in X
xvar = np.sum((pisa.year - pisa.year.mean())**2)
# Compute variance in b1 
s2b1 = (SSE / (y.shape[0] - 2)) / xvar

## 12. Statistical Significance of Coefficients ##

# The variable s2b1 is in memory.  The variance of beta_1

# beta_1_bar = slope
tstat = linearfit.params["year"] / np.sqrt(s2b1)
print(tstat)

## 13. The P-Value ##

# At the 95% confidence interval for a two-sided t-test we must use a p-value of 0.975
pval = 0.975

# The degrees of freedom
df = pisa.shape[0] - 2

# The probability to test against
p = t.cdf(tstat, df=df)
print(p)
beta1_test = True

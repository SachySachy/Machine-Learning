# -*- coding: utf-8 -*-
"""bigData_testing_and_some_regression_graphs.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Fs3U3G0lWLc_3ChCZUHTSs53D0hB_CMU
"""

#Sachin Saigal
#651 test bed for concepts used in actual final code
#115356160
from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import numpy as np
import scipy as sp
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from sklearn.metrics import mean_squared_error
from plotly.subplots import make_subplots
# from sklearn.model_selection import train_test_split
from sklearn import linear_model
# from sklearn import metrics
from xgboost import XGBRegressor
from xgboost import XGBRFRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedKFold
from xgboost import plot_importance

from sklearn.metrics import mean_squared_error, mean_absolute_error, make_scorer, r2_score, mean_absolute_percentage_error
from sklearn.linear_model import LinearRegression, Ridge, Lasso, BayesianRidge, ElasticNet

import sys
file_name = '/content/drive/MyDrive/Real_Estate_Sales_2001-2020_GL_new3.csv'
file = open(file_name)

df = pd.read_csv(file_name)
df.head()

df['Sale Amount'].plot(figsize=(12,5))

fig_bed = make_subplots(rows=1, cols=2)
fig_bed.add_trace(go.Scatter(x=df['List Year'] , y=df['Ratio'] , name='Bed Scatter Plot', mode='markers'), row=1, col=1)
fig_bed.add_trace(go.Box(x=df['List Year'], y=df['Assessed Value'], name='Bed Box Plot'), row=1, col=2)
fig_bed.show()

ax1 = df.plot.scatter(x='Sale Amount',
                      y='Assessed Value',
                      c='DarkBlue')

ax1 = df.plot.scatter(y='Ratio',
                      x='List Year',
                      c='DarkBlue')

towns =df['Town'].unique().tolist()
print(len(towns))
print(towns)

df.groupby(['Town']).plot.scatter(y='Ratio',
                      x='List Year',
                      c='DarkBlue')

df.groupby(['Town']).plot.scatter(y='Assessed Value',
                      x='Sale Amount',
                      c='DarkBlue')

from sklearn.linear_model import LinearRegression

for town_x in towns:
  town_df = df.loc[df.Town== town_x]


  x1 = []
  y1 = []
  sale_x = town_df['Sale Amount']
  for x in sale_x:
   x1.append(x)
  value_y = town_df['Assessed Value']
  for y in value_y:
    y1.append(y)
  print(x1)
  print(y1)

  x1 = np.array(x1).reshape(-1,1)
  y1 = np.array(y1).reshape(-1,1)
  regressor = LinearRegression()
  regressor.fit(x1, y1)

  plt.scatter(x1, y1, color = 'red')
  plt.plot(x1, regressor.predict(x1), color = 'blue')
  plt.title('Sale Amount vs Assessed Value: '  + town_x)
  plt.xlabel('Sale Amount')
  plt.ylabel('Assessed Value')
  plt.show()

for town_x in towns:
  town_df = df.loc[df.Town== town_x]


  x1 = []
  y1 = []
  sale_x = town_df['List Year']
  for x in sale_x:
   x1.append(x)
  value_y = town_df['Ratio']
  for y in value_y:
    y1.append(y)
  print(x1)
  print(y1)

  x1 = np.array(x1).reshape(-1,1)
  y1 = np.array(y1).reshape(-1,1)
  regressor = LinearRegression()
  regressor.fit(x1, y1)

  plt.scatter(x1, y1, color = 'red')
  plt.plot(x1, regressor.predict(x1), color = 'blue')
  plt.title('Year vs Ratio: '  + town_x)
  plt.xlabel('Year')
  plt.ylabel('Ratio')
  plt.show()

from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=3)

for town_x in towns:
  town_df = df.loc[df.Town== town_x]


  x1 = []
  y1 = []
  sale_x = town_df['List Year']
  for x in sale_x:
   x1.append(x)
  value_y = town_df['Ratio']
  for y in value_y:
    y1.append(y)
  print(x1)
  print(y1)


  x1 = np.array(x1).reshape(-1,1)
  y1 = np.array(y1).reshape(-1,1)

  x_poly = poly.fit_transform(x1)
  regressor = LinearRegression()

  poly.fit(x_poly, y1)
  lin2 = LinearRegression()
  lin2.fit(x_poly, y1)


  plt.scatter(x1, y1, color = 'red')
  plt.plot(x1, lin2.predict(poly.fit_transform(x1)),color='blue')
  plt.title('Year vs Ratio: '  + town_x)
  plt.xlabel('Year')
  plt.ylabel('Ratio')
  plt.show()

# failed testing of creating models
from datetime import date
town_df = df.loc[df.Town== 'Woodbridge']
town_df.set_index('Date Recorded')
town_df.index = pd.to_datetime(town_df['Date Recorded'])


trainX = df.index
trainy = df['Ratio']



model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=300)



x1 = []
y1 = []
date_x = town_df['List Year']
for x in date_x:
  x1.append(x)
ratio_y = town_df['Ratio']
for y in ratio_y:
  y1.append(y)
print(x1)
print(y1)

x1 = np.array(x1).reshape(-1,1)
y1 = np.array(y1).reshape(-1,1)


model.fit(x1, y1)



#train =df.loc[df.index < '01-01-2018']
#test =df.loc[df.index >= '01-01-2018']
#for x in train:
# print(x)

# failed testing of creating models
fig, ax = plt.subplots()
sns.boxplot(data=town_df, x='quarter', y='Ratio')
ax.set_title('Ratio by Quarter')

# failed testing of creating models
town_df = df.loc[df.Town=='Woodbridge']
town_df.set_index('Date Recorded')
town_df.index = pd.to_datetime(town_df['Date Recorded'])

train =town_df.loc[town_df.index < '01-01-2018']
test =town_df.loc[town_df.index >= '01-01-2018']
print(test)

# failed testing of creating models
town_df = df.loc[df.Town=='Woodbridge']
town_df.set_index('Date Recorded')
town_df.index = pd.to_datetime(town_df['Date Recorded'])

train =town_df.loc[town_df.index < '01-01-2018']
test =town_df.loc[town_df.index >= '01-01-2018']

train = create_features(train)
test = create_features(test)

feat = ['quarter','year','month']
targ = ['Ratio']

X_train = train[feat]
y_train = train[targ]

X_test = test[feat]
y_test= test[targ]


#print(town_df.columns)
#reg = xgb.XGBRegressor(n_estimators=1000,early_stopping_rounds=50)
reg = xgb.XGBRegressor(n_estimators=100)
reg.fit(X_train, y_train, eval_set=[(X_train, y_train), (X_test, y_test)], verbose=True)

pd.DataFrame(data=reg.feature_importances_, index=reg.feature_names_in_)

test['prediction'] = reg.predict(X_test)
town_df = town_df.merge(test[['prediction']], how='left', left_index =True, right_index =True)

ax = town_df[['Ratio']].plot(figsize =(15,5))
town_df['prediction'].plot(ax=ax, style='.')
plt.legend(['Truth Data', 'Predictions'])
ax.set_title('Woodbridge')
plt.show()

town_df = df.loc[df.Town=='Woodbridge']

town_df.plot.scatter(y='Assessed Value',
                      x='Sale Amount',
                      c='DarkBlue')

sale_x = town_df['Sale Amount']
value_y = town_df['Assessed Value']

regressor = LinearRegression()
sale_x = sale_x.reshape(-1, 1)
regressor.fit(sale_x, value_y)

plt.scatter(sale_x, value_y, color = 'red')
plt.plot(sale_x, regressor.predict(sale_x), color = 'blue')
plt.title('mark1 vs mark2')
plt.xlabel('mark1')
plt.ylabel('mark2')
plt.show()
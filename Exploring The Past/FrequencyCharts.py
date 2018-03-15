
import pandas as pd
import seaborn as sns
import missingno as msno
import os

import matplotlib.pyplot as plt

os.chdir('/home/administrator/Source/IoTDataScience/Data/Bike') # Set working directory


# load the sample training data
train = pd.read_csv('train.csv')


train['datetime']=pd.to_datetime(train['datetime'])
train['year']=train['datetime'].dt.year
train['month']=train['datetime'].dt.month
train['day']=train['datetime'].dt.day
train['hour']=train['datetime'].dt.hour

targets = ["casual", "registered", "count"]
categoricalVariables = ["season", "holiday", "workingday", "weather", "year", "month", "day", "hour" ]
continuousVariables = ["temp", "atemp", "humidity", "windspeed"]



sns.boxplot(data=train[targets], orient="h")
plt.show()

#histogram
fig = plt.figure(figsize=(15,3))
for i, c in enumerate(targets):
    ax = plt.subplot(1,3,i+1)
    sns.distplot(train[c])
fig.tight_layout()
plt.show()


#We can use bar chart or pie chart to visualise the distribution of categorical variables.
fig = plt.figure(figsize=(15,8))
for i, c in enumerate(categoricalVariables):
    ax = plt.subplot(3,3,i+1)
    sns.countplot(x=train[c])
fig.tight_layout()
plt.show()


 
train[continuousVariables].describe()


fig = plt.figure(figsize=(15,5))
for i, c in enumerate(continuousVariables):
    ax = plt.subplot(2,2,i+1)
    sns.distplot(train[c].dropna())
fig.tight_layout()
plt.show()


fig = plt.figure(figsize=(15,10))
for i, c in enumerate(categoricalVariables):
    ax = plt.subplot(3,3,i+1)
    sns.boxplot(x=train[c], y=train["count"])
fig.tight_layout()



#continuous variables 


fig = plt.figure(figsize=(15,10))
for i, c in enumerate(continuousVariables):
    ax = plt.subplot(2,2,i+1)
    sns.regplot(x=train[c], y=train["count"])
fig.tight_layout()


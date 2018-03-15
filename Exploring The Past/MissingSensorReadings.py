# import required python packages 
import pandas as pd
import seaborn as sns
import missingno as msno
import os

import matplotlib.pyplot as plt

os.chdir('/home/administrator/Source/IoTDataScience/Data/Bike') # Set working directory


# load the sample training data
train = pd.read_csv('train.csv')
train.head()
train.info()
train.describe()


#Convert 0s to NULLs


train.loc[train["humidity"]==0, "humidity"]=None
train.loc[train["windspeed"]==0, "windspeed"]=None

msno.matrix(df=train, color = (0.2, 0.5, 0.6))
plt.show()

print(train.isnull().sum().sort_values(ascending=False))
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
import seaborn as sns
import missingno as msno
import os


os.chdir('/home/administrator/Source/IoTDataScience/Data/Bike') # Set working directory


# load the sample training data
train = pd.read_csv('train.csv')


b = []
for i in range(50):
    a = np.random.normal(5,i+1,10)
    b.append(a)

c = np.array(b)

cm =np.corrcoef(c)

plt.imshow(cm,interpolation='nearest')
plt.colorbar()
plt.show()


#heat map
plt.figure(figsize=(17,11))
sns.heatmap(train.iloc[:,1:30].corr(), cmap= 'viridis', annot=True)
plt.show()
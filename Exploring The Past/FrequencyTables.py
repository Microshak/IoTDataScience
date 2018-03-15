import numpy as np
import pandas as pd
import os



os.chdir('/home/administrator/Source/IoTDataScience/Data/Titanic') # Set working directory

titanic_train = pd.read_csv("train.csv")      # Read the data

char_cabin = titanic_train["Cabin"].astype(str)    # Convert cabin to str

new_Cabin = np.array([cabin[0] for cabin in char_cabin]) # Take first letter

titanic_train["Cabin"] = pd.Categorical(new_Cabin)  # Save the new cabin var


my_tab = pd.crosstab(index=titanic_train["Survived"],  # Make a crosstab
                              columns="count")      # Name the count column

print(my_tab)



type(my_tab)  

ByPClass = pd.crosstab(index=titanic_train["Pclass"],  # Make a crosstab
                      columns="count")      # Name the count column


BySex = pd.crosstab(index=titanic_train["Sex"],     # Make a crosstab
                     columns="count")      # Name the count column

#print(ByPClass)
#print(BySex)

cabin_tab = pd.crosstab(index=titanic_train["Cabin"],  # Make a crosstab
                        columns="count")               # Name the count column


print (cabin_tab.sum(), "\n")   # Sum the counts

print (cabin_tab.shape, "\n")   # Check number of rows and cols

print(cabin_tab.iloc[1:7])             # Slice rows 1-6


##CROSS TAB
# Table of survival vs. sex
survived_sex = pd.crosstab(index=titanic_train["Survived"], 
                           columns=titanic_train["Sex"])

survived_sex.index= ["died","survived"]

print(survived_sex)


# Table of survival vs passenger class
survived_class = pd.crosstab(index=titanic_train["Survived"], 
                            columns=titanic_train["Pclass"])

survived_class.columns = ["class1","class2","class3"]
survived_class.index= ["died","survived"]

print(survived_class)



# Table of survival vs passenger class
survived_class = pd.crosstab(index=titanic_train["Survived"], 
                            columns=titanic_train["Pclass"],
                             margins=True)   # Include row and column totals

survived_class.columns = ["class1","class2","class3","rowtotal"]
survived_class.index= ["died","survived","coltotal"]

print(survived_class)

##% and Row sums
print(survived_class/survived_class.ix["coltotal","rowtotal"])


print(survived_class/survived_class.ix["coltotal"])

#Swap ROW and Cols
print(survived_class.T/survived_class["rowtotal"])


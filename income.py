#Bulit model on income data
print("Data science")
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

os.chdir('C:\\Users\\91930\\OneDrive\\Desktop')
data=pd.read_csv('income.csv')
data.dropna(axis=0,inplace=True)
print(data.info())
print(data.select_dtypes(include=[object]))
print(data.describe(include="O"))
data1=data.copy()
print(data1.isnull().sum())
data1["SalStat"]=data1["SalStat"].map({' less than or equal to 50,000':0,' greater than 50,000':1})
print(data1['SalStat'])
new_data=pd.get_dummies(data1,drop_first=True)

col=list(new_data.columns)
#features=list(set(col)-set('SalStat'))
e=set(col)
a=['SatSal']
d=set(a)
features=list(e-d)
y=new_data['SalStat'].values
x=new_data[features].values
train_x,test_x,train_y,test_y=train_test_split(x,y,test_size=0.3, random_state=0)
logistic=LogisticRegression()
logistic.fit(train_x,train_y)
prediction=logistic.predict(test_x)
m=confusion_matrix(test_y,prediction)
print(m)

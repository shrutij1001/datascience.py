import pandas as pd
import numpy as np
from matplotlib import pyplot as pl
import seaborn as sns
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import os
os.chdir('C:\\Users\\91930\\OneDrive\\Desktop')
train_data=pd.read_csv('bank_train.csv')
test_data=pd.read_csv('bank_test.csv')
print(train_data.dtypes)
print("null row",train_data.isnull().sum())
train_data.dropna(axis=0,inplace=True)
test_data.dropna(axis=0,inplace=True)
train_data['deposit']=train_data['deposit'].map({'yes':1,'no':0})
test_data['deposit']=test_data['deposit'].map({'yes':1,'no':0})
train_data1=train_data.copy()
train = pd.get_dummies(train_data, drop_first=True)
test = pd.get_dummies(test_data, drop_first=True)
test1 = test.copy()
train1 = train.copy()
#data1=data.copy()
feature = train.drop(['deposit'], axis=1)
label = train1['deposit']
test_feature = test.drop(['deposit'], axis=1)
test_label = test1['deposit']
#print(train_data['education'].value_counts())
#print(test_data['education'].value_counts())
#print(a.loc[a.loan=='yes'].count())
#print("percentage=",(1227/2171)*100)
#print(train.loc[train.=='yes'].count())
'''print(a)
# KNN model
n=7
kn_classifer=KNeighborsClassifier(n_neighbors=n)
kn_classifer.fit(feature,label)
pred=kn_classifer.predict(test_feature)
accuracy=accuracy_score(test_label,pred)
print(accuracy)
print("misclasiffed:",(test_label!=pred).sum())
#logistic method
logistic=LogisticRegression(random_state=0)
logistic.fit(feature,label)
prediction=logistic.predict(test_feature)
accuracy=accuracy_score(test_label,prediction)
print(accuracy)
print("misclasiffed:",(test_label!=prediction).sum())
cm=confusion_matrix(test_label,prediction)
cm_df=pd.DataFrame(cm,columns=['predicted negative','predicted positive'],index=['actual negative','acutal positive'])
print(cm_df)
tp=cm[1][1]
print("tp:",tp)
tn=cm[0][0]
print("tn:",tn)
fp=cm[0][1]
print("fp:",fp)
fn=cm[1][0]
print("fn:",fn)
print("sensitivity:",tp/(tp+fn))
print("sepecifty:",tn/(tn+fp))
print("precision:",tp/(tp+fp))
print((2*(tp/(tp+fp))*tp/(tp+fn))/(tp/((tp+fn))+tp/(tp+fp)))
logistic=LogisticRegression(random_state=0)
logistic.fit(feature,label)
prediction=logistic.predict(test_feature)
accuracy=accuracy_score(test_label,prediction)
print(accuracy)
print("misclasiffed:",(test_label!=prediction).sum())

print("memory usage-",train_data.memory_usage().sum())
print("ndim",train_data.ndim)
print('shape',train_data.shape)
print(train_data.iat[1,2])
print(train_data.loc[:,'housing'])
print(train_data.select_dtypes(include=float))
#sns.countplot(train_data['marital'],hue=train_data["deposit"])
#pl.show()'''
b=pd.crosstab(index=train_data1['deposit'],
                  columns=train_data1['poutcome'],dropna=True,normalize='columns')
print(b)
print(pd.crosstab(index=train_data['housing'],columns='counts',dropna=True,normalize=True))
sns.regplot(x='age',y='balance',scatter=True,data=train_data)
pl.show()


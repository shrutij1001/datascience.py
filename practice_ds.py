import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.linear_model import LogisticRegression
import os
os.chdir('C:\\Users\\91930\\OneDrive\\Desktop')
'''serviceT=pd.read_csv("ServiceTrain.csv")
test=pd.read_csv("ServiceTest.csv")
print(serviceT)
#serviceT=serviceT.dropna(axis=1,inplace=True)
print(serviceT['Service'])
serviceT['Service']=serviceT['Service'].map({'Yes':1,'No':0})
test['Service']=test['Service'].map({'Yes':1,'No':0})
feature=serviceT.drop(columns='Service',axis=1)
label=serviceT['Service']
test_fea=test.drop(columns='Service',axis=1)
test_label=test['Service']
logistic=LogisticRegression()
logistic.fit(feature,label)
prediction=logistic.predict(test_fea)
acuracy=accuracy_score(test_label,prediction)
print(acuracy)
print("misclassified %d"%(test_label!=prediction).sum())
n=4
knn=KNeighborsClassifier()
knn.fit(feature,label)
prediction=knn.predict(test_fea)
acu=accuracy_score(test_label,prediction)
print(acu)'''
txt=pd.read_csv("milk.txt",sep="\t")
print(txt)
data=txt.select_dtypes(exclude=[object])
data.corr(method='pearson')
martic=data.corr()
print(martic)


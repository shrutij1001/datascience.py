import os
import numpy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
os.chdir('C:\\Users\\91930\\OneDrive\\Desktop')
data=pd.read_csv('income.csv')
print(data.iat[0,0])
print(data)
print(data.loc[1:10,'occupation'])
print(data.select_dtypes(exclude=[object]))
print(data.info())
#print(numpy.unique(data['Cancer']))
print(data)
data.dropna(axis=0,inplace=True)
print(data)
#plt.scatter(data['Cell Shape'],data['Cell Size'],c='red')
#plt.hist(data['Normal Nucleoli'],color='blue',edgecolor='white')
plt.xlabel("normal nucleoli")
plt.ylabel("no. of sample")
count=[900,800,550]
index=np.arange(len(count))
fuel=["pertol","desiel","cng"]
plt.bar(index,count,color=["lightblue","blue","darkblue"])
plt.xlabel("fuel")
plt.ylabel("count")
plt.xticks(index,fuel,rotation=90)
plt.show()
#sns.pairplot(data, kind="hist", hue="Cancer")
#sns.distplot(data['Cell Shape'],kde='True')
#plt.show()
#print(data)
#print(data[data.Cancer==0])
#extr = data.loc[data.isin([0])]
#print(extr)
print(data.describe())
print(data[data.InternetService=='No'])
print(data['tenure'].describe())
print(data['tenure'].mode())
data['tenure'].replace('One',1,inplace=True)
data['tenure'].replace('Four',4,inplace=True)
print(data['SeniorCitizen'].describe())
#Income data
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

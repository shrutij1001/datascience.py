import pandas as pd
import seaborn as sns
from matplotlib import pyplot as pl
data=pd.read_csv(r'C:\\Users\\91930\\OneDrive\\Desktop\car.csv')
#print(data.info())
#print(data.describe())
pd.set_option("display.float_format",lambda x:'%.3f'%x)
#print(data.describe())
#print(data.isnull().sum())
pd.set_option('display.max_columns',500)
print(data.describe())
value=data['powerPS'].value_counts().sort_index()
print(value)
col=['name','postalCode','dateCreated','dateCrawled','lastSeen',]
data=data.drop(columns=col,axis=1)
#sns.regplot(x=data['yearOfRegistration'],y=data['price'],fit_reg=False)
#pl.show()
data=data[(data.yearOfRegistration<=2018) & (data.yearOfRegistration>=1950)&(data.price>=100)
          &(data.price<=15000)&(data.powerPS>=10)& (data.powerPS<=500)
          & (data.kilometer<=150000)& (data.kilometer<=100000)]
sns.distplot(x=data['price'])
sns.boxplot(x=data['price'])
#sns.distplot(x=data['powerPS'])
#sns.boxplot(x=data['powerPS'])
pl.show()
data['age']=(2018-data['yearOfRegistration'])+data['monthOfRegistration']/12
data['age']=round(data['age'],2)
print(data['age'].describe())
data=data.drop(columns=['yearOfRegistration','monthOfRegistration'],axis=1)
#sns.regplot(x='age',y='price',fit_reg=True,scatter=True,data=data,)
sns.distplot(x=data['kilometer'])
pl.show()
pd.crosstab(data['sellar'],normalize=True)
print()
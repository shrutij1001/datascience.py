#from gtts import gTTS
#import os
#mytext ="hello everyone"
#language = 'en'
#myobj = gTTS(text=mytext, lang=language, slow=False)
#myobj.save("shruti.mp3")
#os.system("shruti.mp3")
import numpy as np
import os
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
os.chdir('C:\\Users\\91930\\OneDrive\\Desktop')
data=pd.read_csv('car.csv')
car=data.copy(deep=False)
a=np.unique(car.columns)
print(a)
print(car.isnull().sum())
print(car.describe())
pd.set_option('display.float_format',lambda x:'%.3f'%x)
print(car.describe())
pd.set_option('display.max_columns',500)
print(car.describe())
col=['name','lastSeen','dateCrawled','dateCreated','postalCode']
cars=car.drop(columns=col,axis=1)
cars.duplicated(keep='first')
years=cars['yearOfRegistration'].value_counts().sort_index()
sum(cars['yearOfRegistration']>2018)
sum(cars['yearOfRegistration']>1950)
#sns.regplot(x=cars['yearOfRegistration'],y=cars['price'],scatter=True)
#plt.show()
prices=cars['price'].value_counts().sort_index()

power=cars['powerPS'].value_counts().sort_index()
print(cars['price'].describe())
cars=cars[(cars.yearOfRegistration<=2018)&(cars.yearOfRegistration>=1950)&(cars.price>=100)
          &(cars.price<=150000)&(cars.powerPS>=10)&(cars.powerPS<=500)]
cars['ages']=(2018-cars['yearOfRegistration'])+car['monthOfRegistration']
cars['ages']=round(cars['ages'],2)
cars=cars.drop(columns=['yearOfRegistration','monthOfRegistration'],axis=1)
#age
sns.distplot(cars['ages'])

#plt.show()
cols=['seller','offerType','abtest']
cars.drop(columns=cols,axis=1)
cars_select=cars.select_dtypes(exclude=[object])
correlation=cars_select.corr()
round(correlation,3)
print(cars_select.corr().loc[:,'price'].abs().sort_values(ascending=False)[1:])
cars=cars.dropna(axis=0)
car_omit=pd.get_dummies(cars,drop_first=True)
a=['price']
x1=car_omit.drop(columns=a,axis="columns",inplace=False)
y1=car_omit['price']
y1=np.log(y1)
train_x,train_y,test_x,test_y=train_test_split(x1,y1,test_size=0.3,random_state=3)
print(train_x.shape,test_x.shape,train_y.shape,test_y.shape)
base_pred=np.mean(test_y)
print(base_pred)
base_pred=np.repeat(base_pred,len(test_y))
base_root=np.sqrt(mean_squared_error(test_y,base_pred))
lrg=LinearRegression(fit_intercept=True)
model_lin=lrg.fit(train_x,train_y)
cars_prediction=lrg.predict(test_x)
l=mean_squared_error(test_y,cars_prediction)
r=np.sqrt(l)
#print(r)
r2=model_lin.score(test_x,test_y)
r3=model_lin.score(train_x,train_y)
print(r2,r3)
#0.738720364206519 0.7514527887504687
#print(r2,r3)
resedual=test_y-cars_prediction
sns.regplot(x=cars_prediction,y=resedual,scatter=True,fit_reg=False)
#plt.show()
resedual.describe()
'''
rf=RandomForestRegressor(n_estimators=100,max_features='auto',max_depth=100,min_samples_split=10,min_samples_leaf=4,random_state=1)
model=rf.fit(train_x,train_y)
prediction=rf.predict(test_x)
error=mean_squared_error(test_y,prediction)
root_error=np.sqrt(error)
print(root_error)
r2_rf=model.score(train_x,train_y)
r3_rf=model.score(test_x,test_y)
print('rf1=',r2_rf,'rf2=',r3_rf)
imputed=cars.apply(lambda x:x.fillna(x.median()) if x.dtype=='float' else x.fillna(x.value_counts().index[0]))
print(imputed.isnull().sum())'''
#rf1= 0.8771934710961847 rf2= 0.7910377665239714



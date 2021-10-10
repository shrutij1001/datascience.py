import os
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
os.chdir('C:\\Users\\91930\\OneDrive\\Desktop')
cdata=pd.read_csv('churn.csv', na_values=['1@#'])
#print(cdata[cdata.InternetService == 'Fiber optic'])
#print(cdata.loc[cdata.InternetService=='Fiber optic'])
#print(cdata.loc[cdata.InternetService.isin(['Fiber optic'])])
'''for i in cdata['customerID']:
    if len(i) == 10:
        print(i)'''
count=0
cdata['Dependents'].fillna(cdata["Dependents"].mode()[0],inplace=True)
print(cdata['Dependents'][224])
print(cdata['Dependents'].isnull().sum())
print(cdata['Dependents'].describe())
for i in cdata['Dependents']:
    if i == 'No':
        count+=1
print(count)
gr=dict(height_ratios =(0.15,0.85))
print(gr)
f,(ax_box,ax_hist)=plt.subplots(2,gridspec_kw=gr)
sns.boxplot(cdata['MonthlyCharges'],ax=ax_box)
sns.distplot(cdata['MonthlyCharges'],ax=ax_hist,kde=False)
print(cdata.isnull().sum())
cdata.dropna(axis=0,inplace=True)
print(cdata.isnull().sum())
plt.show()
# -*- coding: utf-8 -*-
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor



career=pd.read_csv('Career_Choices.csv')
df=pd.read_csv('exams (2).csv')


X=df[['aptitude score','test preparation course']]
Y = df[['GradePoints']]

X_train,X_test,Y_train,Y_test =train_test_split(X,Y,test_size=0.3)

rf=RandomForestRegressor()
model=rf.fit(np.array(X_train).reshape(-1,2),np.array(Y_train).reshape(-1,1))

a=int(input())
b=int(input())


r=np.array(rf.predict(np.array([[a,b]])))

if r>=0.9 and r<=1.0 :
    choices = career[['90% - 100%','70% - 90%','50% - 70%','40% - 50%','10% - 40%']]
elif r >=0.7 and r<=0.9:
    choices = career[['70% - 90%','50% - 70%','40% - 50%','10% - 40%']]
elif r>= 0.5 and r<=0.7:
    choices = career[['50% - 70%','40% - 50%','10% - 40%']]
elif r>=0.4 and r<=0.5:
    choices = career[['40% - 50%','10% - 40%']]
else :
    choices =career[['10% - 40%']]
final=choices.values.tolist() 

print(r)

for i in final:
    for h in i:
        print(h)
        

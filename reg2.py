import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
w=pd.read_csv('C:/Users/user/Downloads/startt/startup/50_Startups.csv')
print(w)
w.shape  
w.head()
a=w.drop('Profit',axis=1)
b=w['Profit']
print(a,b)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_split(x,y,test_size=0.2,random_)
from sklearn .linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train,y_train)

print(regressor.intercept_)
print(regressor.coef_)
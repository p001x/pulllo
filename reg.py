import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

v=pd.read_csv('C:/Users/user/Downloads/pinterest/linear.csv')
print(v)


x=v.iloc[:,:-1].values
y=v.iloc[:,1].values

from sklearn.linear_model import LinearRegression
reg=LinearRegression()
reg.fit(x,y)

print(reg.intercept_)
print(reg.coef_)

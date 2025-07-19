import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

v=pd.read_csv('C:/Users/user/Downloads/pinterest/linear.csv')
print(v)
v.head()
v.describe()
v.plot(x='hours',y='scores',style='o')
plt.show()

x=v.iloc[:,:-1].values
y=v.iloc[:,1].values

from sklearn.linear_model import LinearRegression
reg=LinearRegression()
reg.fit(x,y)

print(reg.intercept_)
print(reg.coef_)

y_pred=reg.predict(x)
df=pd.DataFrame({'actual':y,'predicted':y_pred})
df
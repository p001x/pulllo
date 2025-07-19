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
reg=LinearRegression
reg.fit(x,y)

print(reg.intercept)
print(reg.coef_)


from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression(random_state=0)
classifier.fit(xtrain,ytrain)

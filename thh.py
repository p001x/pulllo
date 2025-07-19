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

y_pred=reg.predict(x)
df=pd.DataFrame({'actual':y,'predicted':y_pred})
print(df)

from sklearn.metrics import mean_squared_error,r2_score
print('MSE:%.2f'% mean_squared_error(y,y_pred))
print('R2_score:%.2f'% r2_score(y,y_pred))

plt.scatter(x,y,color='black')
plt.plot(x,y_pred,color='blue',linewidth=2)
plt.show()

import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
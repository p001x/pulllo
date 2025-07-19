import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
from sklearn.metrics import r2_score,mean_squared_error
x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
y=[16.2,33.4,34.6,97.8,590.5,65.9,724.5,590.7,678.5,789.9,890.9,879.89,675.4,323.4,7567.87]

mymodel=np.poly1d(np.polyfit(x,y,1))
myline=np.linspace(1,15,100)
plt.scatter(x,y)
plt.plot(myline,mymodel(myline))
plt.show()
print('R^2 Score is :%.2f'
      %r2_score(y,mymodel(x)))
print('mean squared error:%.2f'
      % mean_squared_error(y,mymodel(x)))




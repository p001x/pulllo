import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd

log=pd.read_csv('C:/Users/user/Downloads/pinterest/framingham.csv')
print(log)
log.shape

x=log.iloc[:,[2,3]].values
print(x)

y=log.iloc[:,4].values
print(y)

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.25)

from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
xtrain=sc_x.fit_transform(xtrain)
xtest=sc_x.transform(xtest)
print(xtrain[0:10,:])

from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression(random_state=0)
classifier.fit(xtrain,ytrain)

y_pred=classifier.predict(xtest)
print(y_pred)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(ytest,y_pred)
print('confusion matrix:\n',cm)

from sklearn .metrics import accuracy_score
print('accuaracy:',accuracy_score(ytest,y_pred))

#second example
import numpy as np
import matplotlib.pyplot as plt 
from scipy import stats

import seaborn as sns ;sns.set()

from sklearn.datasets import fetch_lfw_people
faces=fetch_lfw_people(min_faces_per_person=60)
print(faces.target_names)
print(faces.images.shape)

fig,ax=plt.subplots(5,5)
for i,ax in enumerate(ax.flat):
    axi.imshow(faces.image[i],smap='bone')
    axi.set(xticks=[],yticks=[],
            xlabel=faces.target_names[faces.target[i]])
    



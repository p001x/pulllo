from sklearn.datasets import load_wine
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np
wine=pd.read_csv('C:/Users/user/Downloads/pinterest/archive/wine_data.csv')
wine=load_wine()
x=np.array(wine.data)
y=np.array(wine.target)
print(y)

wine

#applying pca
from sklearn.decomposition import PCA 
pca=PCA(n_components=2)
result=pca.fit(x)
z=result.transform(x)
plt.scatter(z[:,0],z[:,1],c=y)
plt.show()

#applying lda
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
lda=LinearDiscriminantAnalysis()
x_lda=lda.fit_transform(x,y)
plt.scatter(x_lda[:,0],x_lda[:,1],c=y)
plt.show()


from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.3)
lda.fit(xtrain,ytrain)

yn=lda.predict(xtest)
print(ytest)
print(yn)
print(ytest-yn)
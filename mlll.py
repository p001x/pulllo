import numpy as np
import matplotlib.pyplot as plt 
x=np.array([[0,1,2,3,4,5,1,2,3,3,5,6,7,8],[1,2,3,3,5,5,0,1,1,2,3,5,6,6]])
y=np.array([0,0,0,0,0,0,1,1,1,1,1,1,1,1])
x=x.T 
plt.scatter(x[:,0],x[:,1],c=y)
plt.show()

#apply pca
from sklearn.decomposition import PCA
pca=PCA(n_components=1)
pca.fit(x)
xr=pca.transform(x)
print(xr)

#plt
plt.scatter(xr[:,0],xr[:,0],c=y)
plt.show()

#apply lda
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
lda=LinearDiscriminantAnalysis()
x_lda=lda.fit_transform(x,y)
plt.scatter(x_lda[:,0],x_lda[:,0],c=y)
plt.show()

print(x_lda)
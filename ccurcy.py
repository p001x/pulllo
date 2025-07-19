from sklearn import metrics

y=['c','h','f','c','h','f','c','h','h']
y_pred=['c','c','f','h','h','c','c','f','f']

cm=metrics.classification_report(y,y_pred,labels=['c','h','f'])
print(cm)

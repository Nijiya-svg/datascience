import pandas as pd
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix,classification_report
import matplotlib.pyplot as plt

iris = load_iris()
data=pd.DataFrame(iris.data,columns=iris.feature_names)
data['species']=iris.target


x = data.iloc[:, :-1]

kmeans=KMeans(n_clusters=3,random_state=42)
data['cluster']=kmeans.fit_predict(x)

print("Custer Centers:\n",kmeans.cluster_centers_)
print("\nconfusion Matrix:\n",confusion_matrix(data['species'],data['cluster']))
print("\nclassification Report:\n",classification_report(data['species'],data['cluster']))

plt.figure(figsize=(8, 6))
plt.scatter(x.iloc[:, 0], x.iloc[:, 1],c=data['cluster'],cmap='rainbow',s=50)
plt.title('kmeans clustering of iris datasets(k=3)')
plt.xlabel('Sepal.length')
plt.ylabel('Sepal.width')
plt.show()

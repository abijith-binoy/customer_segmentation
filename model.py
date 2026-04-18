from matplotlib import markers
from matplotlib.pyplot import axes
from scipy.sparse import data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv('store_customers.csv')
df.dropna(inplace=True)

#print(df.head())
#print(df.info())

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(df.drop(['Gender','CustomerID'],axis=1))
scaled=sc.transform(df.drop(['Gender','CustomerID'],axis=1))
#print(scaled)
df2 = pd.DataFrame(scaled,columns=df.columns[2:])
#print(df2.head())

#sns.pairplot(data=df2)
#plt.show()

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=4)
kmeans.fit(df2)

centeriods = kmeans.cluster_centers_
labels = kmeans.labels_
print(centeriods)
print(labels)
'''
# Plot the actual data points colored by their cluster label
plt.scatter(df2.iloc[:, 0], df2.iloc[:, 1], c=labels, cmap='viridis', alpha=0.6)

# Plot the centroids on top
plt.scatter(centeriods[:,0], centeriods[:,1], c='red', marker='X',label='Centroids')

plt.xlabel(df2.columns[0])
plt.ylabel(df2.columns[1])
plt.legend()
plt.show()
'''
'''
wcss =[]
for i in range(1,11):
    k=KMeans(n_clusters=i)
    k.fit(df2)
    wcss.append(k.inertia_)
plt.plot(wcss,range(1,11),marker='o')
plt.ylabel('K value')
plt.xlabel('WCSS')
plt.show()
'''
df['cluster']=labels
cluster_means = df.groupby('cluster').mean(numeric_only=True)
print(cluster_means)
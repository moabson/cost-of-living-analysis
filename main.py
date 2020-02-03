from sklearn.cluster import KMeans
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA

dataframe = pd.read_csv("data/cost-of-living-transpose.csv")

# print(dataframe)

features = list(dataframe.columns)[1:]
features_data = dataframe[features]
# 
model = KMeans(n_clusters = 3, init='k-means++', max_iter= 300, n_init = 10, random_state = 0)
dataframe["clusters"] = model.fit_predict(features_data)
# 
print(model.cluster_centers_[:, 0])
print()
print(model.cluster_centers_[:, 1])

print()
print(model.cluster_centers_)

# plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s = 100, c = 'red', label='Careful(c1)')
# plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s = 100, c = 'green', label='Standard(c2)')
# plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s = 100, c = 'blue', label='Target(c3)')
# plt.scatter(model.cluster_centers_[:, 0], model.cluster_centers_[:, 1], s = 250, c = 'yellow', 
#             label='Centroids')
# plt.title("aosdkaosd")
# plt.show()

# 
# dataframe.to_csv("data/result.csv")
# 
# print("done")
# 
# plt.scatter()

reduced_data = PCA(n_components=2).fit_transform(features_data)
results = pd.DataFrame(reduced_data, columns=["pca1","pca2"])

sns.scatterplot(x="pca1", y="pca2", hue=dataframe["clusters"], data=results)

plt.title('K-means Clustering with 2 dimensions')
plt.show()
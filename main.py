from sklearn.cluster import KMeans
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
import numpy as np

dataframe = pd.read_csv("data/cost-of-living-transpose.csv")

# print(dataframe)

N_CLUSTERS = 3

features = list(dataframe.columns)[1:]
features_data = dataframe[features]

model = KMeans(n_clusters = N_CLUSTERS, init='k-means++', max_iter= 300, n_init = 10, random_state = 0)
dataframe["clusters"] = model.fit_predict(features_data)

dataframe.to_csv("data/result.csv")

group_by_clusters = dataframe.groupby("clusters")
average = group_by_clusters.mean()
std = group_by_clusters.std()

i = 0
for feature in features:
    print(feature)
    print(average[feature])
    print(std[feature])
    group_by_clusters.boxplot(column = feature)
    plt.show()
    # plt.savefig("data/fig_" + str(i))
    print()
    i += 1

reduced_data = PCA(n_components=2).fit_transform(features_data)
results = pd.DataFrame(reduced_data, columns=["pca1","pca2"])
  
sns.scatterplot(x="pca1", y="pca2", hue=dataframe["clusters"], data=results)
  
plt.title("K-means clustering with 2 dimensions")
plt.show()


    
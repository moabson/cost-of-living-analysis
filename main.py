from sklearn.cluster import KMeans
import pandas as pd
from matplotlib import pyplot as plt

dataframe = pd.read_csv("data/cost-of-living-transpose.csv")

features = list(dataframe.columns)[1:]
features_data = dataframe[features]

model = KMeans(n_clusters = 5)
dataframe["clusters"] = model.fit_predict(features_data)

print(model.cluster_centers_)

dataframe.to_csv("data/result.csv")

print("done")
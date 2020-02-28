import pandas as pd

dataframe = pd.read_csv("db/model.csv")

# print(dataframe)

for index, row in dataframe.iterrows():
    cluster = int(row["clusters"])
    
    print(cluster)
    
    if cluster == 0:
        row["cluster2"] = 1
    elif cluster == 1:
        row["cluster2"] = 2
    elif cluster == 2:
        row["cluster2"] = 0
        
dataframe['clusters2'] = dataframe.apply(lambda row: 1 if row.clusters == 0 else 2 if row.clusters == 1 else 0, axis = 1) 
          
dataframe.to_csv("db/model_2.csv")


# dataframe["cluster2"] = dataframe.apply(lambda row: row["cluster"]) 



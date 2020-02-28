from flask import Flask, render_template, request
import pandas as pd

country_region_df = pd.read_csv("/home/moabson/eclipse-workspace-python/cost-of-living-analysis/db/map_country_region.csv")
model_df = pd.read_csv("/home/moabson/eclipse-workspace-python/cost-of-living-analysis/db/model_2.csv")

map = dict()

for index, row in country_region_df.iterrows():
#     print(row["country"])
    country, region = row["country"], row["region"]
#     map[country] = region

    if region not in map:
        map[region] = set()

    map[region].add(country)
 
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search', methods = ["POST"])
def search():
    print(request.form)
     
    region = str(request.form["region"])
    student = eval(request.form["student"])
    work = eval(request.form["work"])
    financial = str(request.form["financial"])
    
    print("Region ", region)
    print("Student ", student)
    print("Work ", work)
    print("Financial ", financial)

    cluster = None
    score_student = -1 if student else 0
    score_work = 1 if work else 0
    score_financial = 1 if financial == "Stable" else -1
    
    score = score_student + score_work + score_financial
    
    if score == 0:
        cluster = 2
    elif score > 0:
        cluster = 0
    else:
        cluster = 1
        
    print("Cluster to user: ", cluster)
    print("Score for user: ", score)
    
    data = []
        
    if region in map:
        locations = model_df.loc[model_df["location"].str.contains("|".join(map[region]))]
        locations_filtred_by_cluster = locations.loc[locations["clusters"] == cluster]
        
        for index, row in locations_filtred_by_cluster.iterrows():     
            data.append({
                "id": index,
                "location": row["location"],
                "cluster": row["clusters"]
            })

    return render_template("search.html", data = data)

if __name__ == '__main__':
    app.run(debug=True)
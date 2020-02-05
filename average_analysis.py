import pandas as pd
from scipy.stats import mannwhitneyu
from scipy.stats import kruskal

df = pd.read_csv('data/result.csv')

# print(df['Unnamed: 0.1'])

group_by_clusters = df.groupby("clusters")
average = group_by_clusters.mean()
std = group_by_clusters.std()
count = group_by_clusters.size()

print(count,'\n')

features = list(df.columns)[2:-1]

with open('average_analysis.txt', 'w') as f:
    f.write('Kruskal-Wallis H Test\n\n')
    for feature in features:
        g = []
        for i in range(0, 3):
            a = {'average': average.loc[i, feature], 'std': std.loc[i, feature], 'cluster': i, \
                'data': list(df.loc[df['clusters'] == i][feature])}
            g.append(a)

        g = sorted(g, key=lambda k: k['average'], reverse=True)
        
        s = 0
        for item in g:
            item['class'] = s
            s += 1
        
        stat, p = kruskal(g[0]['data'], g[1]['data'])
        if p > 0.05:
            g[1]['class'] = g[0]['class']
        
        stat, p = kruskal(g[1]['data'], g[2]['data'])
        if p > 0.05:
            g[2]['class'] = g[1]['class']
        else:
            g[2]['class'] = g[1]['class'] + 1
        
        f.write(feature + '\n')
        for item in g:
            f.write('cluster:' + str(item['cluster']) + ', average:'+ str(item['average'])+ ', std:'\
                + str(item['std']) + ', '+ str(item['class']) + '\n')
        
        f.write('\n')


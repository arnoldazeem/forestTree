import pandas as pd
import numpy as np

df1 = pd.read_csv("data1.csv", header=0)

def mapping(e,my_list):
    uniqueVals = np.unique(my_list)
    d = dict([(y, x ) for x, y in enumerate((uniqueVals))])
    df1[e] = df1[e].replace(d)

header = df1.columns.values

for i in header:
    my_list = df1[i].values
    mapping(i, my_list)


df1.to_csv('data_int',sep='\t')

print('done')

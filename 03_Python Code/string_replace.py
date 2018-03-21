import pandas as pd
import numpy as np

df1 = pd.read_csv("data1.csv", header=0)

def mapping(my_list):

    uniqueVals = np.unique(my_list)

    d = dict([(y, x + 1) for x, y in enumerate((uniqueVals))])

    for index,i in enumerate(my_list):
        for name, value in d.items():  # for name, age in list.items():  (for Python 3.x)
            if i == name:
                my_list[index] = value

    return my_list

header = df1.columns.values
for i in header:
    my_list = df1[i].values

    recieved = mapping(my_list)



#df1.apply(mapping, axis=0)

#header = df1.columns.values
#for i in header:
    #my_list = df1[i].values

#uniqueVals = np.unique(my_list)

    #d = dict([(y, x + 1) for x, y in enumerate(sorted(set(uniqueVals)))])

    #print(d)


    #for x, y in enumerate(sorted(set(uniqueVals))):

    #d = dict(y, x + 1)






















#for i in df1.index:
#print(df1.loc[2])



import pickle as pkl
import numpy as np
import pandas as pd
import networkx as nx
import torch
import pandas as pd
import os
treePath = ('data.TD_RvNN.vol_5000.txt')
id_set=set()
start=0
dataDic={}
for line in open(treePath):
    line = line.rstrip()
    eid, indexP, indexC,Vec = line.split('\t')[0], line.split('\t')[1], int(line.split('\t')[2]), line.split('\t')[5]
    if eid not in dataDic.keys():
        dataDic[eid]=[[indexP,indexC,Vec]]
    else:
        dataDic[eid].append([indexP,indexC,Vec])

for key,value in dataDic.items():
    with open("./txt5000/"+key+".txt","w") as f:
        for value1 in value:
            f.write(str(value1))


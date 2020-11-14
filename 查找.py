#-*- codeing = utf-8 -*-
#@Time:2020/9/17 10:37
#@Author:邵东延
#@File:查找.py
#@software:PyCharm
import csv
from pandas.core.frame import DataFrame
import numpy as np
import pandas as pd

tmp_lst = []
with open('YUANSHUJU.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        tmp_lst.append(row)
df = pd.Da
taFrame(tmp_lst[1:], columns=tmp_lst[0])
print(df)data =pd.read_csv('YUANSHUJU.csv', encoding= "gbk")
print(data)
source_data=pd.read_csv("VF.csv")
cha=pd.read_csv("VF.csv",encoding="gbk")
print(cha)

list=source_data.values.tolist()
list1=data.values.tolist()
print(list)

with open("result2.txt","a+") as f:
 for i in list:
    for j in i:
        for h in list1:
            for b in h:
             if j==b :
                 f.write(j)
                 f.write(" ")
                 f.write(str(h[1]))
                 f.write("\n")

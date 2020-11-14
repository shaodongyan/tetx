import numpy as np
import pandas as pd

import pandas as pd
import numpy as np

# 读取整个csv文件
csv_data = pd.read_csv("/Users/shaodongyan/PycharmProjects/pythondemo/dejun/two-is.csv")

print(csv_data)

# 读取指定列索引字段的数据
#csv_data = pd.read_csv("./stock_day.csv", usecols=['open', 'close'])

# 将我们修改完的csv的文件保存到新的路径下
#csv_data.to_csv('demo.csv')
h=len(csv_data)
h=h
print(len(csv_data))
print(csv_data.iat[1,1])
for i in range (0,h):
    print(i)
    filename="/Users/shaodongyan/PycharmProjects/pythondemo/dejun/"+csv_data.iat[i,0]+".fasta"
    with open(filename,"a+") as f :
        f.write(">")
        f.write(csv_data.iat[i,0])
        f.write("\n")
        f.write(csv_data.iat[i,1])
        f.write("\n")


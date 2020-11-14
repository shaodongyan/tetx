#-*- codeing = utf-8 -*-
#@Time:2020/7/7 22:37
#@Author:邵东延
#@File:tubian.py
#@software:PyCharm
import copy
d={'1':"A",
   "2":"T",
   "3":"C",
   "4":"G"}
cishu=0
dic={}
dic[1]="A"
dic[2]="T"
dic[3]="C"
dic[4]="G"
dictu={}
dictu[1]=[2,3,4]
dictu[2]=[1,3,4]
dictu[3]=[1,2,4]
dictu[4]=[1,2,3]
xulie=(2,3,2,2,1,1,4,1,1,1,2,2)
xuliea=[]
xuliea=[2,3,2,2,1,1,4,1,1,1,2,2]
tubian1=[]
for i in range(0,12):
    for c in range(0,3):
        tubian=[2,3,2,2,1,1,4,1,1,1,2,2]
        tubian[i]=dictu[xulie[i]][c]
        print(tubian)
        for b in range(i+1,12):
            for d in range(0,3):
                tubian2=copy.copy(tubian)
                tubian2[b]=dictu[xulie[b]][d]
                print("diyicitubian")
                print(tubian)
                print("diercitubian")
                print(tubian2)
                cishu = cishu + 1
                with open('7.7_21.txt', 'a+') as f:
                    f.write(">")
                    #f.write(str(cishu)+" "+str((i+1))+" tubian"+str((c+1))+' '+"dier"+str((b+1))+' '+"tubian"+str((d+1)))
                    f.write(str(cishu))
                    f.write("\n")
                    for e in range(0,12):
                        f.write(dic[tubian2[e]])
                    f.write("\n")








#!/usr/bin/python
# coding: UTF-8

res_list = []
f = open('score.csv','r')
line = f.readlines()
for data in line:
    a = data.split(",")[2]
    res_list.append(float(a))

print res_list
print "要素数",len(res_list)
print "合計" ,sum(res_list)
print "平均",sum(res_list)/len(res_list)
f.close



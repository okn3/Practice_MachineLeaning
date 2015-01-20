#!/usr/bin/python
# coding: UTF-8
 
f = open('score.csv')
line = f.readlines()
for data in line:
    print data.split(",")[2]
f.close


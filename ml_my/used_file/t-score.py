# coding: utf-8
import math, csv

data = []
#input_data = input("スコア手動入力 >")

f = open("score.csv","r")
f_line = f.readlines()
for d_line in f_line:
    a = d_line.split(",")[2]
    data.append(float(a))
f.close

#data.append(input_data)

num = len(data)
print "original data\n",data #debag
#print num #debag

_sum = sum(data)
average = _sum/num
print "score平均", average #debug

subtraction = []
for p in data:
    subtraction.append(p - average)

variances = 0
for p in subtraction:
    variances += p ** 2
variances /= float(num)

standerd_deviation = math.sqrt(variances)

print "標準偏差",standerd_deviation

if standerd_deviation == 0:
    print "all 50"
else:
    for p in subtraction:
        deviation = 50 + p * 10.0 / float(standerd_deviation)
#        print "%d" % deviation
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print "このグループの平均顔面偏差値 : [ %d ]" % deviation
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"


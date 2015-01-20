# coding: utf-8
import math
num = int(input())
data = []

_sum = 0
for i in range(num):
    ipt = int(input())
    data.append(ipt)
    _sum += ipt
average = _sum/num

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
        devitaion = 50 + p * 10.0 / float(standerd_deviation)
        print "%d" % devitaion



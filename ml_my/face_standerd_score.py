#-*- coding:utf-8 -*-
#########################
#
# 顔面偏差値平均算出プログラム
#
##########################
import json, urllib2, os, csv
import moduleTscore as tm

beauty_sum = 0
age_sum = 0
emtion_sum = 0
a = 0 
line = "============================="

"""ジャンル指定プログラム
genre = input("指定なし:0 ミスコン:1 ミスター:2 サークル:3 >")
if genre == 0:
    f = open('score.csv', 'a')
elif genre == 1:
    f = open('misscon.csv', 'a')
elif genre == 2:
    f = open('mister.csv', 'a')
elif genre == 3:
    f = open('circle.csv', 'a')
else:
    print "select error"
"""

f = open('score.csv', 'a')
writer = csv.writer(f)

print line
print "Analyze faces standerd score."
print line

API_KEY = 'mdJOxGSyeVnL43er' #rekognitionAPIキー
API_SECRET = 'qRocUKPjfcKa7P1J' #rekognitionAPIシークレット
pic_url = raw_input("Input image URL >") #画像のURLを入力
jobs = 'face_age_beauty_emotion'
group_name = raw_input("Input group name >")
url = 'http://rekognition.com/func/api/?api_key=' + API_KEY + '&api_secret=' + API_SECRET + '&jobs=' + jobs + '&urls=' + pic_url
r = urllib2.urlopen(url) #URLを開く
root = json.loads(r.read()) #結果をロードする
#print(root) #デバッグ用
#print "url: "+url #デバッグ用

for key in root[u'face_detection']:
#    print key #デバッグ用
    beauty_score = key[u'beauty']*100
    print a+1 ,"人目"
    print "beauty:" , beauty_score #綺麗さ
    print "age:" ,  key[u'age'] #年齢
    #print "emotion:" ,  key[u'emotion'] #気分
    beauty_sum += beauty_score
    age_sum += key[u'age']
    a += 1

print "============Score============"
print "グループ名",group_name
print "メンバー:", a, "人"
print "顔面評価:",str.format('{0:.1f}', beauty_sum/a),"point"
print "平均年齢:",str.format('{0:.1f}', age_sum/a)
print line
writer.writerow([group_name,a,int(beauty_sum/a),int(age_sum/a)])
f.flush()
f.close

ts = tm.calcTscore()

print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print "このグループの平均顔面偏差値 : [ %d ]" % ts
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
 

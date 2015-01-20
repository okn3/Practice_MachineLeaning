#-*- coding:utf-8 -*-
#########################
#
# face or things + analysis
#
##########################
import json, urllib2, os

print "facedetect & analysis"
API_KEY = 'mdJOxGSyeVnL43er' #rekognitionAPIキー
API_SECRET = 'qRocUKPjfcKa7P1J' #rekognitionAPIシークレット
pic_url = raw_input("Input image URL >") #画像のURLを入力
target = raw_input("human:0 or things:1 >") #解析多少の選択

if target == "0" or target == "human" :
    jobs = raw_input("select face+[part,age,gender,beauty,race,motion,glass] \n EXAMPLE: face_age_beauty \n >") #分析項目の選択
elif target == "1" or target == "things" : 
    jobs = 'scene_understanding_3'
else:
    print "select error."

url = 'http://rekognition.com/func/api/?api_key=' + API_KEY + '&api_secret=' + API_SECRET + '&jobs=' + jobs + '&urls=' + pic_url
r = urllib2.urlopen(url) #URLを開く
root = json.loads(r.read()) #結果をロードする

print(root)
print "url: "+url

#cmd = "open "+ url
#os.system(cmd) #出力がうまくいかない

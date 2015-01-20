#-*- coding:utf-8 -*-
import json, urllib2

API_KEY = '1234'
API_SECRET = '5678'
jobs = 'face_age_beauty' #アルゴリズムの種類,faceやscene_understanding_3
pic_url = 'http://pic.prepics-cdn.com/smapphoto/12756846.jpeg' #解析したい画像のURL
url = 'http://rekognition.com/func/api/?api_key=' + API_KEY + '&api_secret=' + API_SECRET + '&jobs=' + jobs + '&urls=' + pic_url

r = urllib2.urlopen(url) #URLを開く
root = json.loads(r.read()) #結果をロードする
print(root)
print(root[u'face_detection'][0][u'age'])#年齢を表示
print(root[u'face_detection'][0][u'beauty'])#美しさを表示

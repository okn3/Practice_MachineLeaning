#-*- coding:utf-8 -*-
import json, urllib2

API_KEY = 'mdJOxGSyeVnL43er'
API_SECRET = 'qRocUKPjfcKa7P1J'
jobs = 'face_recognize' #アルゴリズムの種類,faceやscene_understanding_3
pic_url = 'http://livedoor.blogimg.jp/toua2chdqn/imgs/5/8/58781bbe.jpg' #解析したい画像のURL
url = 'http://rekognition.com/func/api/?api_key=' + API_KEY + '&api_secret=' + API_SECRET + '&jobs=' + jobs + '&urls=' + pic_url

r = urllib2.urlopen(url) #URLを開く
root = json.loads(r.read()) #結果をロードする
print(root)
print(root[u'face_detection'][0][u'name'])#類似度の結果を表示
print(url)

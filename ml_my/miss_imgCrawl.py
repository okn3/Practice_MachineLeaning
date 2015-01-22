# coding: utf-8

import urllib
import BeautifulSoup
import sys

import createFaceDB

link_data = []
def getLink():
    #url = sys.argv[1]
#    url = raw_input("URL >")
    url = "http://misscolle.com"
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup.BeautifulSoup(html)
    data = soup.find(id="gfoot")
    for list_url in data.findAll('li'):
        T = list_url.a
        links = url + T.get("href")
        #link_data.append(links)
        #print links
        getImageUrl(links)
#    print link_data
    #return link_data

def getImageUrl(link):
    url = link
    html =urllib.urlopen(url).read()
    soup = BeautifulSoup.BeautifulSoup(html)
    data = soup.find(id="contest_key_visual")
    for img_url in data.findAll('img'):
        miss_img = url[:20] + img_url.get('src')
        print miss_img
        createFaceDB.createDB(miss_img,"test")        
#getImageUrl()
getLink()

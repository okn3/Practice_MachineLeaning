# coding: utf-8
import urllib
import BeautifulSoup
import createCSV as CC

file_name = "mr.csv"

def getLink():
    url = "http://mrcolle.com/"
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup.BeautifulSoup(html)
    data = soup.find(id="gfoot")
    for list_url in data.findAll('li'):
        T = list_url.a
        title = T.string
        links = url + T.get("href")
        getImageUrl(links,title)

def getImageUrl(links,title):
    name = title
    html =urllib.urlopen(links).read()
    soup = BeautifulSoup.BeautifulSoup(html)
    data = soup.find(id="contest_key_visual")
    for img_url in data.findAll('img'):
        miss_img = links[:20] + img_url.get('src')
        CC.dataIn(miss_img,name,file_name)

getLink()

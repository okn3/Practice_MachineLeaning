# coding: utf-8

import urllib
import BeautifulSoup
import sys

def main():
    #url = sys.argv[1]
    url = raw_input("URL >")
#    url = "http://misscolle.com/missaoyama2014"
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup.BeautifulSoup(html)
    #print soup.find('title').string
#    print soup.img['src'] #url抜き出し
    for img_url in soup.findAll('img'):
        print url+ (img_url.get('src'))

#    return soup
main()

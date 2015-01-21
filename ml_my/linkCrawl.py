# coding: utf-8

import urllib
import BeautifulSoup
import sys

link_data = []
def main():
    #url = sys.argv[1]
#    url = raw_input("URL >")
    url = "http://misscolle.com"
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup.BeautifulSoup(html)
    data = soup.find(id="gfoot")
    for list_url in data.findAll('li'):
        T = list_url.a
        link_data.append(url + T.get('href'))
    print link_data
    return link_data
main()

#!/usr/bin/python3
#!coding:utf-8

import requests
from bs4 import BeautifulSoup

def getPage(url):
    resp = requests.get(url)
    resp.encoding = 'ascii'
    return resp.text

def getFreeSs(page):
    soup = BeautifulSoup(page)
    lis = soup.find_all("div",class_="hover-text")
    for li in lis:
        json = li.find_all("h4")
        server = json[0].span.string
        server_port = json[1].span.string[0:5]
        password = json[2].span.string[0:8]
        method = json[3].string[7:]
        jsons.append({"method": method,"password": password,"remarks": "du","server": server,"server_port": int(server_port),"local_address":"127.0.0.1","localPort": 1080})

def main():
    global jsons
    jsons = []
    url= "https://global.ishadowx.net/"
    page = getPage(url)
    getFreeSs(page)
    count = 0
    for json in jsons:
        count +=1
        with open("ss_conig_"+str(count)+".json","w") as f:
            f.write(str(json).replace("'",'"'))

if __name__ == "__main__":
    main()

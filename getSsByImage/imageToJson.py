#!/usr/bin/env python3
#!coding:utf-8
import urllib.request, sys,base64,json,os,time,string,re
from PIL import Image
from aip import AipOcr
import time

def apiAuth():
    APP_ID = '10866470'
    API_KEY = 'F99xCchaR1K2NoU1UplBai9b'
    SECRET_KEY = 'z09ANghFCxcs60PGKESE5RDQuLerFrx2'
    return AipOcr(APP_ID, API_KEY, SECRET_KEY)

def cutPic():
    im = Image.open(r"./temp.png")

    img_size = im.size
    w = im.size[0]
    h = im.size[1]
    # print("xx:{}".format(img_size))
    region1 = im.crop((445,300, w-650,335))    #裁剪的区域
    region2 = im.crop((445,335, w-650,370))    #裁剪的区域
    region3 = im.crop((445,370, w-650,405))    #裁剪的区域
    region4 = im.crop((445,405, w-650,440))    #裁剪的区域
    region5 = im.crop((445,440, w-650,475))    #裁剪的区域
    region6 = im.crop((445,475, w-650,510))    #裁剪的区域
    region7 = im.crop((445,520, w-650,555))    #裁剪的区域

    region1.save(r"./crop_test1.png")
    region2.save(r"./crop_test2.png")
    region3.save(r"./crop_test3.png")
    region4.save(r"./crop_test4.png")
    region5.save(r"./crop_test5.png")
    region6.save(r"./crop_test6.png")
    region7.save(r"./crop_test7.png")

def get_json(filePath):
    with open(filePath, 'rb') as fp:
        image = fp.read()
        respon = client.basicGeneral(image)   #用完500次后可改 respon = client.basicAccurate(image) 这个还可用50次
        print(respon)
        titles = respon['words_result']          #获取问题
        try:
            server = titles[0]['words']
            server_port = titles[1]['words']
            password = titles[2]['words']
            method = titles[3]['words']
            if method[0:1] == " ":
                method = method[1:]
            jsons.append({"method": method,"password": password,"remarks": "du","server": server,"server_port": int(server_port),"local_address":"127.0.0.1","localPort": 1080})
        except Exception:
            pass
def downJson():
    num = 0
    for json in jsons:
        num +=1
        with open("./ss_conig_"+str(num)+".json","w") as f:
            f.write(str(json).replace("'",'"'))
def main():
    start = time.time()

    global jsons
    jsons = []

    global client
    client = apiAuth()
    cutPic()

    get_json(r"./crop_test1.png")
    time.sleep(2)
    get_json(r"./crop_test2.png")
    time.sleep(2)
    get_json(r"./crop_test3.png")
    time.sleep(2)
    get_json(r"./crop_test4.png")
    time.sleep(2)
    get_json(r"./crop_test4.png")
    time.sleep(2)
    get_json(r"./crop_test5.png")
    time.sleep(2)
    get_json(r"./crop_test6.png")
    time.sleep(2)
    get_json(r"./crop_test7.png")
    downJson()
    end = time.time()
    print('程序用时：'+str(end-start)+'秒')

if __name__ == "__main__":
    main()

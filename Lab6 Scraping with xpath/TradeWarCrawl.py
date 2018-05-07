# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 21:52:22 2018
多个不同搜索关键字并行爬取
tips：需要一次运行整个脚本，一句句运行无法使用并行

@author: situ
"""
from selenium import webdriver                #selenium实现自动化
from urllib.parse import urlencode
from multiprocessing import Pool
from lxml import etree
import pandas as pd
import os
import requests
import re
import numpy as np

def crawl(para):
    compRawStr = para[0]
    startpage = para[1]
    n = para[2]
    d = {'q': compRawStr.encode('gbk')}
    word = urlencode(d)
    newsData = pd.DataFrame()
    for i in list(range(startpage,startpage+n)):
        url = 'http://search.sina.com.cn/?%s&range=all&c=news&num=20&col=1_7&page=%s' % (word, str(i))
        result = requests.get(url)
        result.encoding = 'gbk'
        selector = etree.HTML(result.text)  
        for item in selector.xpath('//*[@id="result"]/div/div'):
            newsdict = {"title":[0],"date":[0],"time":[0],"source":[0],
                        "abstract":[0],"detail":[0],"href":[0],"origin_url":[0]}
            onenews = pd.DataFrame(newsdict)
#            onenews = pd.DataFrame(np.zeros(8).tolist(),
#                                   columns=["title","date","time","source","abstract","detail","href","orgin_url"])
            onenews["title"] = item.xpath('h2/a')[0].xpath("string(.)")
            print(onenews["title"][0])
            onenews["abstract"]  = item.xpath('p')[0].xpath("string(.)")
            otherinfo = item.xpath('h2/span/text()')[0]
            onenews["source"] , onenews["date"] , onenews["time"]  = otherinfo.split()
            onenews["href"]  = item.xpath('h2/a/@href')[0]
            onenews["origin_url"] ,onenews["detail"] = crawl_con(onenews["href"][0])
            newsData = newsData.append(onenews)
    newsData.to_csv(compRawStr+"_"+str(startpage)+"_"+str(n)+"相关新闻.csv",index = False,encoding = "gb18030")

def crawl_con(href):
    site = requests.get(href)
    site=site.content
    response = etree.HTML(site)
    try:
        origin_url = response.xpath('//*[@id="top_bar"]/div/div[2]/a/@href')[0] 
        detail = "\n".join(response.xpath('//div[@class="article"]/div/p/text()'))+"\n".join(response.xpath('//div[@class="article"]/p/text()'))+"\n".join(response.xpath('//div[@class="article"]/div/div/text()'))
    except:
        origin_url =""
        detail =""
    detail = re.sub('\u3000', '', detail)    #全角的空白符
    return origin_url,detail



if __name__=='__main__':
    os.chdir("E:/graduate/class/Statistical Case Studies/homework6")
    print('请输入您想爬取内容的关键字：')
    compRawStr = input('关键字1 关键字2： \n')     #键盘读入 多个关键字则用空格隔开
    PageN = input('起始页,页数： \n')     #如键盘读入 1,5 1,5
    print('正在爬取“' + compRawStr.capitalize()+ '”有关新闻!')
    comp = compRawStr.split()
    pn = PageN.split()
    para = []
    if (len(comp)==len(pn)) & (len(comp)>1):#多个关键词
        l = len(comp) #多进程爬取不同搜索词新闻
        for i in range(l):
            para.append([comp[i]]+[int(c) for c in pn[i].split(",")])   
            #[['中美贸易战', 1, 5], ['外交部', 1, 5]]
#        crawl(comp[0]) #爬取成功会输出title
        #crawl(['中美贸易战', 1, 5])
    if (len(comp)==len(pn)) & (len(comp)==1):#一个关键词，页面并行爬取
        l=3
        sp,n = [int(i) for i in pn[0].split(",")]
        sep = int(round(n/l,0))
        para = [[comp[0],sp,sep],[comp[0],sp+sep,sep],[comp[0],sp+2*sep,n-(sp+2*sep)]]
    p=Pool(l)
    p.map(crawl,para)       #爬取4页内容
    p.close()
    p.join()
    print("爬取成功，请打开"+os.getcwd()+"查看详情")





# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 21:52:22 2018
改成类
多个不同搜索关键字并行爬取
tips：需要一次运行整个脚本，一句句运行无法使用并行

@author: situ
"""
from selenium import webdriver                #selenium实现自动化
from urllib.parse import urlencode
from lxml import etree
import pandas as pd
import os
import requests
import re
import numpy as np

class crawl(object):
    def __init__(self,compRawStr = "",startpage = 1, n = 5):
        self.startpage  = startpage 
        self.n = n
        self.compRawStr = compRawStr

    def crawlmain(self):
        compRawStr = self.compRawStr
        startpage = self.startpage
        n = self.n
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
                onenews["title"] = item.xpath('h2/a')[0].xpath("string(.)")
                print(onenews["title"][0])
                onenews["abstract"]  = item.xpath('p')[0].xpath("string(.)")
                otherinfo = item.xpath('h2/span/text()')[0]
                onenews["source"] , onenews["date"] , onenews["time"]  = otherinfo.split()
                onenews["href"]  = item.xpath('h2/a/@href')[0]
                onenews["origin_url"] ,onenews["detail"] = self.crawl_con(onenews["href"][0])
                newsData = newsData.append(onenews)
        return newsData
#        newsData.to_csv(compRawStr+"_"+str(startpage)+"_"+str(n)+"相关新闻.csv",index = False,encoding = "gb18030")

    def crawl_con(self,href):
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


def main():
    os.chdir("E:/graduate/class/Statistical Case Studies/homework6")
    print('请输入您想爬取内容的关键字：')
    compRawStr = input('关键字： \n')     #键盘读入 多个关键字则用空格隔开
    PageN = input('起始页 页数： \n') #键盘输入 空格隔开
    print('正在爬取“' + compRawStr.capitalize()+ '”有关新闻!')
    search1 = crawl()
    search1.compRawStr = compRawStr
    search1.startpage,search1.n = [int(i) for i in PageN.split()]
    result = search1.crawlmain()
    result.to_csv(search1.compRawStr+"_"+str(search1.startpage)+"_"+str(search1.n)+"相关新闻.csv",
                  index = False,encoding = "gb18030")
    print("爬取成功，请打开"+os.getcwd()+"查看详情")
    
if __name__ == '__main__':
    main()    
    






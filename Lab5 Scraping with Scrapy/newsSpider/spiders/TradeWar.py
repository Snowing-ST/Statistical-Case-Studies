# -*- coding: utf-8 -*-

#先在prompt里到指定文件夹（如homework5）输入scrapy startproject newsSpider
#在./homework5/newsSpider/newsSpider/spiders/下，输入scrapy genspider TraderWar search.sina.com.cn

import scrapy
from newsSpider.items import NewsspiderItem

class TradewarSpider(scrapy.Spider):
    name = "TradeWar"
#    allowed_domains = ["search.sina.com.cn"]
    start_urls = [
            'http://search.sina.com.cn/?q=%D6%D0%C3%C0%C3%B3%D2%D7%D5%BD&c=news&from=index&col=&range=&source=&country=&size=&time=&a=&page='+'%s&pf=2131425448&ps=2134309112&dpc=1' % p for p in list(range(1,20)) #页数
            ]

    def parse(self, response):
        for href in response.xpath('//*[@id="result"]/div/div/h2/a/@href'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_detail)
            
    def parse_detail(self, response):
        print(response.status)
        print(response.xpath('//h1[@class="main-title"]/text()').extract()[0]) #标题
        news = NewsspiderItem()
        news["url"] = response.url
        news["title"] = response.xpath('//h1[@class="main-title"]/text()').extract()[0]
        news["time"] = response.xpath('//*[@id="top_bar"]/div/div[2]/span/text()').extract()[0]
        news["origin"] = response.xpath('//*[@id="top_bar"]/div/div[2]/a/text()').extract()
        news["origin_url"] = response.xpath('//*[@id="top_bar"]/div/div[2]/a/@href').extract()[0]
        news["detail"] = "\n".join(response.xpath('//div[@class="article"]/div/p/text()').extract())+\
        "\n".join(response.xpath('//div[@class="article"]/p/text()').extract())+\
        "\n".join(response.xpath('//div[@class="article"]/div/div/text()'))
        yield news
#在newsSpider/newsSpider文件夹下运行scrapy crawl TradeWar -o detail2.csv -s FEED_EXPORT_ENCODING=gbk
#在spiders目录下运行scrapy runspider TradeWar.py -o tw.csv -s FEED_EXPORT_ENCODING=gbk


#draft------------------------------------------------------------------


#import requests
#from lxml import etree
#result = requests.get(
#        "http://search.sina.com.cn/?q=%D6%D0%C3%C0%C3%B3%D2%D7%D5%BD&range=all&c=news&sort=rel&col=&source=&from=&country=&size=&time=&a="
#                      )
#result.encoding = 'gbk'
#selector = etree.HTML(result.text)        
#
##一爬一整页的 ]
#url = []
#source_time = []
#title = []
#abstract = []
#newslist = selector.xpath('//*[@id="result"]/div/div')
#for newsitem in newslist:
#    url.extend(newsitem.xpath('h2/a/@href'))
#    source_time.extend(newsitem.xpath('h2/span/text()'))
#    title.append(newsitem.xpath('h2/a')[0].xpath("string(.)"))
#    abstract.append(newsitem.xpath('p')[0].xpath("string(.)"))
#    print(url)
#    print(newsitem.xpath('h2/a')[0].xpath("string(.)"))
#    
#    
#    
#title = selector.xpath('//*[@id="result"]/div/div/h2/a')
#for i in range(len(title)):
#    print(title[i].xpath("string(.)"))
#abstract = selector.xpath('//*[@id="result"]/div/div/p');
#for i in range(len(abstract)):
#    print(abstract[i].xpath("string(.)")) #0要跳过
#urls = selector.xpath('//*[@id="result"]/div/div/h2/a/@href');urls
#source_time = selector.xpath('//*[@id="result"]/div/div/h2/span/text()');source_time
#
#link = []
#pages = selector.xpath('//*[@id="_function_code_page"]/a')
#for page in pages[:(len(pages)-1)]:
#    link.extend(page.xpath('@href'))
#link #并不是完整的url 


#result = requests.get("http://finance.sina.com.cn/money/bond/research/2018-04-13/doc-ifyteqtq9127286.shtml")
#result = requests.get("http://finance.sina.com.cn/money/future/agri/2018-04-13/doc-ifyteqtq9293495.shtml")
#result = requests.get("http://finance.sina.com.cn/china/2018-04-13/doc-ifyteqtq9203074.shtml")
#result = requests.get("http://news.sina.com.cn/c/2018-04-10/doc-ifyuwqez7807075.shtml")
#result = requests.get("http://news.sina.com.cn/o/2018-04-07/doc-ifyuwqez5991820.shtml")
#result.encoding = 'utf-8'
#selector = etree.HTML(result.text)         
#title = selector.xpath('//h1[@class="main-title"]/text()');title 
#time = selector.xpath('//*[@id="top_bar"]/div/div[2]/span/text()');time
#origin = selector.xpath('//*[@id="top_bar"]/div/div[2]/a/@href');origin
#detail =  "\n".join(selector.xpath('//div[@class="article"]/div/p/text()'));print(detail)
#detail =  "\n".join(selector.xpath('//div[@class="article"]/p/text()'));print(detail)
#detail =  "\n".join(selector.xpath('//div[@class="article"]/div/div/text()'));print(detail)
#
#article = selector.xpath('//div[@class="article"]')[0].xpath("string(.)").strip()
#print(article)



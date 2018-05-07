# -*- coding: utf-8 -*-
import scrapy
from newsSpider.items import NewsAbsspiderItem


class TradewarlistSpider(scrapy.Spider):
    name = "TradeWarList"
    allowed_domains = ["search.sina.com.cn"]
    start_urls = ["http://search.sina.com.cn/?q=%D6%D0%C3%C0%C3%B3%D2%D7%D5%BD&range=all&c=news&sort=rel"]

    def parse(self, response):
        # 请求第一页
        yield scrapy.Request(response.url, callback=self.parse_next)

#         请求其它页
        for page in response.xpath('//*[@id="_function_code_page"]/a')[:9]:
            link = response.urljoin(page.xpath('@href').extract()[0])
            print(link)
            yield scrapy.Request(link, callback=self.parse_next)

    def parse_next(self, response):
        for item in response.xpath('//*[@id="result"]/div/div'):
            news = NewsAbsspiderItem()
            print(item.xpath('h2/span/text()').extract()[0])
            news['title'] = item.xpath('h2/a')[0].xpath("string(.)").extract()[0]
            news['abstract'] = item.xpath('p')[0].xpath("string(.)").extract()[0]
            news['source'] = item.xpath('h2/span/text()').extract()[0]
            news['time2'] = item.xpath('h2/span/text()').extract()[0]
            news["url"] = item.xpath('h2/a/@href').extract()[0]
            yield news
#cd /d E/\graduate/class/Statistical Case Studies/homework5/newsSpider/newsSpider/spiders
#scrapy runspider TradeWarList.py -o twlist.csv -s FEED_EXPORT_ENCODING=gbk
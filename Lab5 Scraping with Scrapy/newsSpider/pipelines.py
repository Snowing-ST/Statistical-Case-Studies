# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#每次跑哪个代码，就在setting里指定开启哪个pipeline
class NewsspiderPipeline(object):
    def process_item(self, item, spider):
        item["time"] = item["time"][:11]
        item["detail"] = item["detail"].strip()
        return item

class NewsAbsspiderPipeline(object):
    def process_item(self, item, spider):
        a = item["time2"]
        item["time2"] = a[len(a)-19:][:10]
        item["source"] = a[:len(a)-20]
        return item
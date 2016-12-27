# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TestscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #pass

    #小说的名字
    name = scrapy.Field()
    #小说的作者
    author = scrapy.Field()
    #小说地址
    novelurl = scrapy.Field()
    #小说状态
    serialstatus = scrapy.Field()
    #小说连载字数
    serialnumber = scrapy.Field()
    #文章类别
    category = scrapy.Field()
    #小说编号
    name_id = scrapy.Field()

class DcontentItem(scrapy.Item):

    #小说编号
    id_name = scrapy.Field()
    #章节内容
    chaptercontent = scrapy.Field()

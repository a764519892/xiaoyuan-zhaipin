# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XiaoyuanZhaopinItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    zhiwei =scrapy.Field()
    #xingzhi =scrapy.Field()
    chengshi =scrapy.Field()
    zhaopinrenshu =scrapy.Field()
    fabushijian =scrapy.Field()
    gongsi =scrapy.Field()
    leixing =scrapy.Field()
    wenjian_mingcheng =scrapy.Field()
    pass

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class TeamItem(scrapy.Item):
	selfName = scrapy.Field()
	matchIDs = scrapy.Field()
	time = scrapy.Field()
	oppoName = scrapy.Field()
	winner = scrapy.Field()
	score = scrapy.Field()
	BO = scrapy.Field()
	leagues = scrapy.Field()

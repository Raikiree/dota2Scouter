import scrapy
from team.items import TeamItem

class matchSpider(scrapy.Spider):
	name = 'match'
	allowed_domains = ['dotabuff.com']
	MASKstart_urls = [
					
        "http://www.dotabuff.com/esports/teams/teamid",
       
	]

	start_urls = [m + "/matches?date=all&faction=radiant" for m in MASKstart_urls]
	def parse(self, response):
		#init the item
		item = TeamItem()
		#Get self team name        
		selfName = response.xpath("/html/body/div[1]/div[7]/div[2]/div[1]/div/div[2]/h1/text()").extract()
		match_all = []
		time_init_all = []
		bo_all = []
		league_all = []

		for i in range(20):
			time = response.xpath("//article/table/tbody/tr[" + str(i+1) +"]/td[2]/span/time/text()").extract()
			matcheIdUrl = response.xpath("//article/table/tbody/tr[" + str(i+1) +"]/td[2]/div/a/@href").extract()
			###### Add to Items ######
			match_all.append(matcheIdUrl[0].split('/')[2])
			time_init_all.append(time[0])

		item['selfName'] = selfName[0]
		item['matchIDs'] = match_all
		item['time'] = time_init_all

		yield item
		print('item found!')
		
		




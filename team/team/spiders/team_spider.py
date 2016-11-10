import scrapy
from team.items import TeamItem


class teamSpider(scrapy.Spider):
	name = 'team'
	allowed_domains = ['dotabuff.com']
	start_urls = [

		#team home url
        "http://www.dotabuff.com/esports/teams/teamid",

	]

	def parse(self, response):
		#init the item
		item = TeamItem()

		#Get self team name
		selfName = response.xpath("/html/body/div[1]/div[7]/div[2]/div[1]/div/div[2]/h1/text()").extract()
		#Get the first match  #This is a test feature
		firstMatch = response.xpath("//article/table/tbody/tr[1]/td[2]/div/a/@href").extract()
		#Get all matches series page url in current page: Ex. ~/esports/series/160952'
		seriesURLs = response.xpath("//article/table/tbody/tr/td[2]/div/a/@href").extract()

		#Get all winners
		#Notice: this does not include the tied case in bo2
		winners = response.xpath("//article/table/tbody/tr/td[@class='winner series-winner']/div/a/text()").extract()
		#Get score
		#winning team always put first place
		scoreRaw = response.xpath("//article/table/tbody/tr/td[4]/div[1]/text()").extract()
		score = []
		for s in scoreRaw: 
			tmp = s[0] + ' - ' + s[-1]
			score.append(tmp)

		#Get opponent team names
		oppoTeam = response.xpath("//article/table/tbody/tr/td[@class='series-teams']/div/span[@class='r-none-mobile']/a/text()").extract()


		match_all = []
		time_init_all = []
		bo_all = []
		league_all = []

		for i in range(10):
			league = response.xpath("//article/table/tbody/tr[" + str(i*3+1) +"]/td[1]/a/@href").extract()
			time = response.xpath("//article/table/tbody/tr[" + str(i*3+1) +"]/td[3]/div[2]/small/time/text()").extract()
			bo = response.xpath("//article/table/tbody/tr[" + str(i*3+1) +"]/td[2]/div[1]/a/text()").extract()
			matcheIdUrls = response.xpath("//article/table/tbody/tr[" + str(i*3+1) +"]/td[6]/div/span/a/@href").extract()

			###### Process Details ######
			#process macheIDs
			serieMatches = []
			for url in matcheIdUrls:
				serieMatches.append(url.split('/')[2])
			#process leagues
			lea = league[0].split('/')[-1]

			###### Add to Items ######
			bo_all.append(bo)
			match_all.append(serieMatches)
			time_init_all.append(time)
			league_all.append(lea)

		item['selfName'] = selfName[0]
		item['oppoName'] = oppoTeam
		item['matchIDs'] = match_all
		item['winner'] = winners
		item['time'] = time_init_all
		item['score'] = score 
		item['leagues'] = league_all

		yield item
		print('item found!')
		
		
	






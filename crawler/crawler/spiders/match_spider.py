import scrapy
import re

class MatchSpider(scrapy.Spider):
    name = 'match'

    def start_requests(self):
        for year in range(2013,2023):
            for month in range(1,13):
                for day in range(1,32):
                    url = f'https://www.espn.in/football/scoreboard/_/league/eng.1/date/{year}{month:02}{day:02}'
                    yield scrapy.Request(url, self.parse)

    def parse(self, response):
        json_string = response.xpath('//script[contains(., "window.espn.scoreboardData")]/text()').get()
        match_ids = re.findall('_/gameId/[\d]+', json_string)
        for id in match_ids:
            url = f'https://www.espn.in/football/match/{id}'
            yield scrapy.Request(url, self.parseMatch)

    def parseMatch(self, response):
        data = dict()
        data['date'] = response.xpath('//div[@data-module="gameInformation"]//span/@data-date').getall()[0][0:10]
        # data['S'] = response.xpath('//div[@class="game-details header"]/text()').getall()[0].strip('\n\t ')
        data['home'] = response.xpath('//span[@class="long-name"]/text()').getall()[0]
        data['away'] = response.xpath('//span[@class="long-name"]/text()').getall()[1]
        data['home_goal'] = int(response.xpath('//span[@data-home-away="home"][@data-stat="score"]/text()').getall()[0].strip('\n\t '))
        data['away_goal'] = int(response.xpath('//span[@data-home-away="away"][@data-stat="score"]/text()').getall()[0].strip('\n\t '))
        shot_data_home = response.xpath('//span[@data-home-away="home"][@data-stat="shotsSummary"]/text()').getall()
        shot_data_away = response.xpath('//span[@data-home-away="away"][@data-stat="shotsSummary"]/text()').getall()
        data['home_shot'] = int(shot_data_home[0].split(' ')[0])
        data['away_shot'] = int(shot_data_away[0].split(' ')[0])
        data['home_shot_on_goal'] = int(shot_data_home[0].split(' ')[1][1:-1])
        data['away_shot_on_goal'] = int(shot_data_away[0].split(' ')[1][1:-1])
        data['home_possesion_pct'] = int(response.xpath('//span[@data-home-away="home"][@data-stat="possessionPct"]/text()').getall()[0][0:-1]) / 100
        data['away_possesion_pct'] = int(response.xpath('//span[@data-home-away="away"][@data-stat="possessionPct"]/text()').getall()[0][0:-1]) / 100
        data['home_corner'] = int(response.xpath('//td[@data-home-away="home"][@data-stat="wonCorners"]/text()').getall()[0])
        data['away_corner'] = int(response.xpath('//td[@data-home-away="away"][@data-stat="wonCorners"]/text()').getall()[0])
        # data['HF'] = int(response.xpath('//td[@data-home-away="home"][@data-stat="foulsCommitted"]/text()').getall()[0])
        # data['AF'] = int(response.xpath('//td[@data-home-away="away"][@data-stat="foulsCommitted"]/text()').getall()[0])
        # data['HY'] = int(response.xpath('//td[@data-home-away="home"][@data-stat="yellowCards"]/text()').getall()[0])
        # data['AY'] = int(response.xpath('//td[@data-home-away="away"][@data-stat="yellowCards"]/text()').getall()[0])
        # data['HR'] = int(response.xpath('//td[@data-home-away="home"][@data-stat="redCards"]/text()').getall()[0])
        # data['AR'] = int(response.xpath('//td[@data-home-away="away"][@data-stat="redCards"]/text()').getall()[0])
        yield data

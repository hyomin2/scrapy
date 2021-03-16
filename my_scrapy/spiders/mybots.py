import scrapy
from my_scrapy.items import MyScrapyItem
import time
from selenium import webdriver

class MybotsSpider(scrapy.Spider):

  
    name = 'mybots'
    allowed_domains = ['http://www.lotteimall.com']
    pit_data = ['반팔', '민소매', '반바지', '원피스', '셔츠', '면바지', '가디건', 
    '긴팔티', '청바지', '니트', '맨투맨', '자켓', '야상', '니트', '코트', '히트텍', '패딩']
    start_urls = []
    for i in pit_data:
        text_url = 'http://www.lotteimall.com/search/searchMain.lotte?slog=80060_1&headerQuery=' + i + '&lvl1_cate_no=&lvl2_cate_no=&lvl3_cate_no=&lvl4_cate_no=&lvl5_cate_no=&cate_depth=1&selected_filter=&rccode=pc_detail4'
        start_urls.append(text_url)

    # 결과값
    def parse(self, response):
        items = []

        iname = response.xpath('//*[@id="contents"]/fieldset[2]/div/div[3]/ul/li/p[1]/a/text()').extract()
        iprice = response.xpath('//*[@id="contents"]/fieldset[2]/div/div[3]/ul/li/p[2]/strong/text()').extract()
        ireview = response.xpath('//*[@id="contents"]/fieldset[2]/div/div[3]/ul/li/p[4]/span/a/strong/text()').extract()
        
        # print(iname)
        # print(iprice)
        # print(ireview)
        
        
        # print(len(iname))
        # print(len(iprice))
        # print(len(ireview))

        for i in range(len(iname)):
            item = MyScrapyItem()
            item['iname'] = iname[i]
            item['iprice'] = iprice[i]
            item['ireview'] = ireview[i]
            items.append(item)

        return items

        

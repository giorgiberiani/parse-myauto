import scrapy
import requests
import csv
import re
from my_auto.helpers.myauto_helper import MyAutoHelper
from my_auto.helpers.item_helper import ItemHelper

class MyAutoScraper(scrapy.Spider, ItemHelper, MyAutoHelper):
    name = 'myauto'

 

    start_url = 'https://www.myauto.ge/ka/search/?stype=0&currency_id=3&det_search=0&ord=1&category_id=m0&page=1'
    page = requests.get(start_url)
    sel = scrapy.Selector(page)
    number_of_pages = sel.xpath('/html/body/div[2]/div/div[2]/div[1]'
                                '/div[3]/ul/li[6]/a/@href').extract_first()
    number_of_pages = int(number_of_pages.split('=')[-1])
    print(number_of_pages)

    def start_requests(self):
           
        url = 'https://www.myauto.ge/ka/search/?stype=0&currency_id=3&det_search=0&ord=1&category_id=m0&page={}'

        for i in range(1, 3):
            yield scrapy.Request(url=url.format(i), callback=self.parse)

    def parse(self, response):

        cars = response.xpath('//h4/a/@href').extract()
        for url in cars:
            yield scrapy.Request(url = url, callback = self.parse_content )


    def parse_content(self, response):

        if  response.xpath('/html/body/div[2]/div/div[6]/div[1]/div[5]/div[1]/div[2]/div[1]/span/text()').extract_first() != ' აუქციონის ჩატარების თარიღი: '\
            and response.xpath('//*[@class="det-property"]//text()').extract_first() != ' ქირავდება ':

            self.helper_respnse = response
            
            item = self.make_item(
                    customs= self.get_customs(),
                    location = self.get_location(),
                    manufacturer = self.get_manufacturer(),
                    model = self.get_model(),
                    year = self.get_year(),
                    category = self.get_category(),
                    fuel_type = self.get_fuel_type(),
                    engine_volume = self.get_engine_volume(),
                    mileage = self.get_mileage(),
                    cylinders = self.get_cylinders(),
                    gear_type = self.get_gear_type(),
                    drive_wheels = self.get_drive_wheels(),
                    doors = self.get_doors(),
                    wheel = self.get_wheel(),
                    color = self.get_color(),
                    interior_color = self.get_interior_color(),
                    airbags = self.get_airbags(),
                    abs = self.get_abs(),
                    el_windows = self.get_el_windows(),
                    air_condintioner = self.get_air_condintioner(),
                    climate_system = self.get_climate_system(),
                    leather_interior = self.get_leather_interior(),
                    disks = self.get_disks(),
                    navigation_system = self.get_navigation_system(),
                    central_lock = self.get_central_lock(),
                    hatch = self.get_hatch(),
                    alarm = self.get_alarm(),
                    board_computer = self.get_board_computer(),
                    hydraulics = self.get_hydraulics(),
                    anti_skid = self.get_anti_skid(),
                    chair_warming = self.get_chair_warming(),
                    parking_control = self.get_parking_control(),
                    rear_view_camera = self.get_rear_view_camera(),
                    price = self.get_price(),
                    description = self.get_description())

        
   
            yield item

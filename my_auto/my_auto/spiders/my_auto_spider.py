import scrapy
import requests
import csv
from .helper import Helper
import json


class MyAutoScraper(Helper, scrapy.Spider):
    name = 'myauto'

    file_path = '/home/alo/Desktop/Data/myauto_cars.csv'


    with open(file_path, 'w') as csvfile:
        fieldnames = ['Customs',
                      'Manufacturer',
                      'Model',
                      'Year',
                      'Category',
                      'Fuel Type',
                      'Engine Volume',
                      'Mileage',
                      'Cylinders',
                      'Geaer Type',
                      'Drive Wheels',
                      'Doors',
                      'Wheel',
                      'Color',
                      'Interior Color',
                      'Airbags',
                      'ABS',
                      'El Windows',
                      'Air Condintioner',
                      'Climate System',
                      'Leather Interior',
                      'Disks',
                      'Navigation System',
                      'Central Lock',
                      'Hatch',
                      'Alarm',
                      'Board Computer',
                      'Hydraulics',
                      'Anti skid',
                      'Chair Warming',
                      'Parking Control',
                      'Rear View Camera',
                      'Price']

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()


    file_path = '/home/alo/Desktop/Data/cars.csv'
    myFile = open(file_path, 'w')

    def start_requests(self):
        start_url = 'https://www.myauto.ge/ka/search/?stype=0&' \
                    'currency_id=3&det_search=0&ord=1&category_id=m0&page=1'
        page = requests.get(start_url)
        sel = scrapy.Selector(page)
        number_of_pages = sel.xpath('/html/body/div[2]/div/div[2]/div[1]'
                                    '/div[3]/ul/li[6]/a/@href').extract_first()
        number_of_pages = int(number_of_pages.split('=')[-1])

        urls = []

        for i in range(1,10):
            urls.append('https://www.myauto.ge/ka/search/?stype=0&'
                        'currency_id=3&det_search=0&ord=1&category_id=m0&page={}'.format(i))

        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):

        cars = response.xpath('//h4/a/@href').extract()
        for url in cars:
            yield scrapy.Request(url = url, callback = self.parse_content )


    def parse_content(self, response):


        price = response.xpath('//*[@class="car-price " or @class="car-price resized" or @class="no-fixed-price"]/text()').extract_first()
        manufacturer = response.xpath('//*[@class="detail-car-table"]//tr[1]/th[1]/div[2]//text()').extract_first()
        model = response.xpath('//*[@class="detail-car-table"]//tr[2]/th[1]/div[2]//text()').extract_first()
        year = response.xpath('//*[@class="detail-car-table"]//tr[3]/th[1]/div[2]//text()').extract_first()
        category = response.xpath('//*[@class="detail-car-table"]//tr[4]/th[1]/div[2]//text()').extract_first()
        fuel_type = response.xpath('//*[@class="detail-car-table"]//tr[5]/th[1]/div[2]//text()').extract_first()
        engine_volume = response.xpath('//*[@class="detail-car-table"]//tr[6]/th[1]/div[2]//text()').extract_first()
        mileage = response.xpath('//*[@class="detail-car-table"]//tr[7]/th[1]/div[2]//text()').extract_first()
        cylinders = response.xpath('//*[@class="detail-car-table"]//tr[8]/th[1]/div[2]//text()').extract_first()
        gear_type = response.xpath('//*[@class="detail-car-table"]//tr[9]/th[1]/div[2]//text()').extract_first()
        drive_wheels = response.xpath('//*[@class="detail-car-table"]//tr[10]/th[1]/div[2]//text()').extract_first()
        doors = response.xpath('//*[@class="detail-car-table"]//tr[11]/th[1]/div[2]//text()').extract_first()
        wheel = response.xpath('//*[@class="detail-car-table"]//tr[12]/th[1]/div[2]//text()').extract_first()
        color = response.xpath('//*[@class="detail-car-table"]//tr[13]/th[1]/div[2]//text()').extract_first()
        interior_color = response.xpath('//*[@class="detail-car-table"]//tr[14]/th[1]/div[2]//text()').extract_first()
        airbags = response.xpath('//*[@class="detail-car-table"]//tr[15]/th[1]/div[2]//text()').extract_first()
        customs = response.xpath('//*[@class="levy"]//text()').extract_first()

        if response.xpath('//*[@class="detail-car-table"]//tr[1]/th[2]/div[2]/i[@class="fa fa-check"]'):
            abs = True
        else:
            abs = False

        if response.xpath('//*[@class="detail-car-table"]//tr[2]/th[2]/div[2]/i[@class="fa fa-check"]'):
            el_windows = True
        else:
            el_windows = False

        if response.xpath('//*[@class="detail-car-table"]//tr[3]/th[2]/div[2]/i[@class="fa fa-check"]'):
            air_condintioner = True
        else:
            air_condintioner = False

        if response.xpath('//*[@class="detail-car-table"]//tr[4]/th[2]/div[2]/i[@class="fa fa-check"]'):
            climate_system = True
        else:
            climate_system = False

        if response.xpath('//*[@class="detail-car-table"]//tr[5]/th[2]/div[2]/i[@class="fa fa-check"]'):
            leather_interior = True
        else:
            leather_interior = False

        if response.xpath('//*[@class="detail-car-table"]//tr[6]/th[2]/div[2]/i[@class="fa fa-check"]'):
            disks = True
        else:
            disks = False

        if response.xpath('//*[@class="detail-car-table"]//tr[7]/th[2]/div[2]/i[@class="fa fa-check"]'):
            navigation_system = True
        else:
            navigation_system = False

        if response.xpath('//*[@class="detail-car-table"]//tr[8]/th[2]/div[2]/i[@class="fa fa-check"]'):
            central_lock = True
        else:
            central_lock = False

        if response.xpath('//*[@class="detail-car-table"]//tr[9]/th[2]/div[2]/i[@class="fa fa-check"]'):
            hatch = True
        else:
            hatch = False

        if response.xpath('//*[@class="detail-car-table"]//tr[10]/th[2]/div[2]/i[@class="fa fa-check"]'):
            alarm = True
        else:
            alarm = False

        if response.xpath('//*[@class="detail-car-table"]//tr[11]/th[2]/div[2]/i[@class="fa fa-check"]'):
            board_computer = True
        else:
            board_computer = False

        if response.xpath('//*[@class="detail-car-table"]//tr[12]/th[2]/div[2]/i[@class="fa fa-check"]'):
            hydraulics = True
        else:
            hydraulics = False

        if response.xpath('//*[@class="detail-car-table"]//tr[13]/th[2]/div[2]/i[@class="fa fa-check"]'):
            anti_skid = True
        else:
            anti_skid = False

        if response.xpath('//*[@class="detail-car-table"]//tr[14]/th[2]/div[2]/i[@class="fa fa-check"]'):
            chair_warming = True
        else:
            chair_warming = False

        if response.xpath('//*[@class="detail-car-table"]//tr[15]/th[2]/div[2]/i[@class="fa fa-check"]'):
            parking_control = True
        else:
            parking_control = False

        if response.xpath('//*[@class="detail-car-table"]//tr[16]/th[2]/div[2]/i[@class="fa fa-check"]'):
            rear_view_camera = True
        else:
            rear_view_camera = False

        file_path = '/home/alo/Desktop/Data/myauto_cars.csv'

        lis = [customs, manufacturer, model, year, category, fuel_type,
               engine_volume, mileage, cylinders, gear_type, drive_wheels,
               doors, wheel, color, interior_color, airbags, abs, el_windows,
               air_condintioner, climate_system, leather_interior, disks,
               navigation_system, central_lock, hatch, alarm, board_computer,
               hydraulics, anti_skid, chair_warming, parking_control,
               rear_view_camera, price]
        myFile = open(file_path, 'a')
        with myFile:
            writer = csv.writer(myFile)
            writer.writerow(lis)

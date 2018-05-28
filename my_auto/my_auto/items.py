# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyAutoItem(scrapy.Item):

    customs = scrapy.Field()
    location = scrapy.Field()
    manufacturer =scrapy.Field()
    model =scrapy.Field()
    year =scrapy.Field()
    category =scrapy.Field()
    fuel_type =scrapy.Field()
    engine_volume =scrapy.Field()
    mileage =scrapy.Field()
    cylinders =scrapy.Field()
    gear_type =scrapy.Field()
    drive_wheels =scrapy.Field()
    doors =scrapy.Field()
    wheel =scrapy.Field()
    color = scrapy.Field()
    interior_color = scrapy.Field()
    airbags = scrapy.Field()
    abs = scrapy.Field()
    el_windows = scrapy.Field()
    air_condintioner = scrapy.Field()
    climate_system = scrapy.Field()
    leather_interior = scrapy.Field()
    disks = scrapy.Field()
    navigation_system = scrapy.Field()
    central_lock = scrapy.Field()
    hatch = scrapy.Field()
    alarm = scrapy.Field()
    board_computer = scrapy.Field()
    hydraulics = scrapy.Field()
    anti_skid = scrapy.Field()
    chair_warming = scrapy.Field()
    parking_control = scrapy.Field()
    rear_view_camera = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()




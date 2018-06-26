# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv


class MyAutoPipeline(object):
    def __init__(self):
        file_path = '/home/beriani/Desktop/myauto/data.csv'

        csvfile = open(file_path, 'w')
        fieldnames = ['customs',
                    'location',
                    'manufacturer',
                    'model',
                    'year',
                    'category',
                    'fuel_type',
                    'engine_volume',
                    'mileage',
                    'cylinders',
                    'gear_type',
                    'drive_wheels',
                    'doors',
                    'wheel',
                    'color',
                    'interior_color',
                    'airbags',
                    'abs',
                    'el_windows',
                    'air_condintioner',
                    'climate_system',
                    'leather_interior',
                    'disks',
                    'navigation_system',
                    'central_lock',
                    'hatch',
                    'alarm',
                    'board_computer',
                    'hydraulics',
                    'anti_skid',
                    'chair_warming',
                    'parking_control',
                    'rear_view_camera',
                    'price',
                    'description']
        self.writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        self.writer.writeheader()


    def process_item(self, item, spider):
        self.writer.writerow(item)
        return item

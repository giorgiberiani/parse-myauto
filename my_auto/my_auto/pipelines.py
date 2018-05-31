# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from my_auto.databases.database import MyAutoDB

class MyAutoPipeline(object):
    def __init__(self):

        print("Initializing Pipeline")

        self.connection = MyAutoDB('localhost',
                                    'postgres',
                                    'toor',
                                    'postgres',
                                    '5432')
        self.connection.create_table('carstable')


    def process_item(self, item, spider):
        self.connection.insert('carstable', item)
        return item

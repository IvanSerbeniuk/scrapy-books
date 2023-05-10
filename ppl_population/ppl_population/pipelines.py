# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import logging
import sqlite3


class SQLite3PPLPipeline:
    def open_spider(self, spider):
        self.connection = sqlite3.connect('transcripts.db')
        self.c = self.connection.cursor()
        try:
            self.c.execute('''  
                CREATE TABLE transcripts(
                country TEXT,
                year TEXT,
                population TEXT
                )
            ''')
            self.connection.commit()
        except sqlite3.OperationalError:
            pass


    def close_spider(self, spider):
        self.connection.close()
    
    def process_item(self, item, spider):
        self.c.execute('''
            INSERT INTO transcripts (country,year,population) VALUES(?,?,?)
        ''',(
            item.get('country'),
            item.get('year'),
            item.get('population'),
        ))
        self.connection.commit()
        return item

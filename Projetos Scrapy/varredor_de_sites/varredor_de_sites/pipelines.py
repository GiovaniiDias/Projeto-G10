# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3


class SQLitePipeline(object):
    def open_spider(self, spider):
        self.connection = sqlite3.connect('proxies.db')
        self.cursor = self.connection.cursor()
        # criar tabela
        self.cursor.execute('''
             CREATE TABLE IF NOT EXISTS  proxies(
                proxy_name TEXT NOT NULL PRIMARY KEY,
                domain TEXT,
                country TEXT,
                speed TEXT,
                popularity NUMBER       
              )               
        ''')
        self.connection.commit()

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        self.cursor.execute('''
             INSERT OR IGNORE INTO proxies(proxy_name,domain,country,speed,popularity) VALUES(?,?,?,?,?) 
    ''', (
        item.get('proxy_name'),
        item.get('domain'),
        item.get('country'),
        item.get('speed'),
        item.get('popularity'),
    ))
        self.connection.commit()
        return item

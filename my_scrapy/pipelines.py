# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
import time
from datetime import datetime, timezone
from kafka import KafkaProducer
from json import dumps

class MyScrapyPipeline:
    def __init__(self):
        pass

    # 데이터베이스에 저장하고자하는 코드를 이곳에 입력하면 된다.
    def process_item(self, item, spider):
        print("- - - - - - - - - - - - - - - - - - - -")
        self.storeDB(item)
        print("Success ------------------")
        return item


    def storeDB(self, item):
        prod = KafkaProducer(
            acks = 0,
            compression_type = 'gzip',
            bootstrap_servers = ['54.157.164.90:9092'],
            value_serializer = lambda x : dumps(x).encode('utf-8')
        )
        for i in item:
            data = {"schema":{"type":"struct","fields":[{"type":"string","field":"iname"},{"type":"string","field":"iprice"},{"type":"string","field":"ireview"}],"name":"my_hyomin_pit"},"payload":{"iname":i['iname'],"iprice":i['iprice'],"ireview":i['ireview']}}
            prod.send('my_hyomin_pit', value = data)
            prod.flush()

        print('Done, ')



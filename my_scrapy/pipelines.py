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
        # print("- - - - - - - - - - - - - - - - - - - -")
        # print(item)
        # print("- - - - - - - - - - - - - - - - - - - -")
        # print("- - - - - - - - - - - - - - - - - - - -")
        self.storeDB(item)
        # print("Success ------------------")
        return item


    def storeDB(self, item):
        prod = KafkaProducer(
            acks = 0,
            compression_type = 'gzip',
            bootstrap_servers = ['127.0.0.1:9092'],
            value_serializer = lambda x : dumps(x).encode('utf-8')
        )

        data = {"schema":{"type":"struct","fields":[{"type":"int32","optional":'false',"field":"id"},{"type":"string","optional":'false',"field":"iname"},{"type":"string","optional":'false',"field":"iprice"},{"type":"string","optional":'false',"field":"ireview"}],"optional":'false',"name":"test_pit"},"payload":{"id":700,"iname":item['iname'],"iprice":item['iprice'],"ireview":item['ireview']}}
        prod.send('my_test_pit', value = data)
        time.sleep(1)
        print('data push !')
        prod.flush()

        print('Done, ')



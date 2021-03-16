import os
import time

# os.system('cd {}'.format(os.getcwd()))
# output = os.popen('pip install pymysql').read()
# print(output)

# os.system('cd {}'.format(os.getcwd()))
# output = os.popen('conda install -c scrapinghub scrapy').read()
# print(output)

while True:
    os.system('cd {}'.format(os.getcwd()))
    output = os.popen('scrapy crawl mybots').read()
    print(output)

    print("Timer Start 10sec -----------")
    time.sleep(3600)
    print("Timer over ------------------")

    
from kafka import KafkaProducer
import json
import os
import time
from sys import argv
 
producer = KafkaProducer(bootstrap_servers='192.168.120.11:9092')
 
def log(str):
    t = time.strftime(r"%Y-%m-%d_%H-%M-%S",time.localtime())
    print("[%s]%s"%(t,str))
 
def list_file(path):
    dir_list = os.listdir(path)#grabbing and saving as .json format, then send them one by one. # I will adjust it later if we use data from .json
    for f in dir_list:
         producer.send('world',f)
         producer.flush()
         log('send: %s' % (f))
 
list_file(argv[1])
producer.close()
log('done')

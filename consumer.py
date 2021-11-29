
 
from kafka import KafkaConsumer
import time
 
def log(str):
        t = time.strftime(r"%Y-%m-%d_%H-%M-%S",time.localtime())
        print("[%s]%s"%(t,str))
 
log('start consumer')
#consuming "world" from "192.168.120.11:9092" -- the Topic; "consumer group" is "consumer-20171017"

consumer=KafkaConsumer('world',group_id='consumer-20171017',bootstrap_servers=['192.168.120.11:9092'])
for msg in consumer:
        recv = "%s:%d:%d: key=%s value=%s" %(msg.topic,msg.partition,msg.offset,msg.key,msg.value)#getting info from consumer which can be input into database directly
        log(recv)
        
        
        



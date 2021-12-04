from time import sleep
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:  
                         dumps(x).encode('utf-8'))

#for e in range(1000):
    #data = {'number' : e}
   # producer.send('gb760', value=data)

import yaml
with open('tweet_json_file.json') as f:
    for line in f:
        d = yaml.safe_load(line)
        jd = json.dumps(d)
        producer.send_messages(b'gb760',jd)

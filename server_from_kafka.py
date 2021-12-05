
from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
    'gb760',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: x.decode('utf-8'))

#for message in consumer:
    #print(message)
    


def process_data():        
        
    for message in consumer:
        
        content = json.loads(mseeage) #"load" -- converting to json  #data receiving from producer
        date = content['created_at'].split('T')[0]  #processing data to get CreationDate from json
        hour = content['created_at'].split('T')[1].split(':')[0] #processing data to get CreationHour from json
        min = content['created_at'].split('T')[1].split(':')[1]  #processing data to get CreationMinute from json
        sec = content['created_at'].split('T')[1].split(':')[2]  #processing data to get CreationSeconds from json
        
    return date,hour,min,sec,text  #processing data to get text from json
    
def send_to_db():

    print ("succed!")#待补充
    
if __name__ == '__main__'：

    creatDate,creatHour,creatMin,creatSec,text = process_data()
    send_to_db()





#Lack of datebase conf info 



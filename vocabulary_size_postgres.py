import psycopg2
import connection
import pandas as pd
import re

#read data from database tweets_info
connection = psycopg2.connect(dbname="gb760", user="gb760")  
cursor = connection.cursor()
connection.commit()
# Fetch result
cursor.execute("SELECT * from Tweets_Table")
record = cursor.fetchall()
df = pd.DataFrame(record)
#print("Result ", df)
cursor.close()
connection.close()
print("PostgreSQL connection was ran and closed")

#read tweets in the current minute
cur_m = df.iloc[0,2]
cur_df = df.loc[df[2] == cur_m]
cur_text = df[df.columns[4]]
for i in '!"#$%&()*+-,-./:;<=>?@“”[\\]^_{|}~':
            cur_text = cur_text.replace(i, "") 
cur_text = re.sub('[\.][\.][\.]', '', str(cur_text))
cur_text = re.sub('\d+\s|\s\d+\s|\s\d+', '', str(cur_text))
cur_text = str(cur_text)
cur_text = set(cur_text.split())
un = len(cur_text)
print ("Unique Words in Current Minute Are:")
print (cur_text)
print("Number of Unique Words is:", un)
#compute unique vocabulary from tweets contents


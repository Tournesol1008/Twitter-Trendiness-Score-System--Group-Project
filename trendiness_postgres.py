#Read Word Input

import argparse
parser = argparse.ArgumentParser(description='Count word frequency')
parser.add_argument('--word', help='Take as input a word or phrase')
args = parser.parse_args() 

#run word count file
import sys 
import os
sys.path.append(os.path.abspath("/home/gb760/Group5-760"))
from word_count_postgres import * #use word_count to test
#from word_count_postgres import *
#from vocabulary_size_postgres import *
#run unique word file

#Total number of phrases in the current minute
import psycopg2
import connection
import pandas as pd
#read data from database tweets_info
connection = psycopg2.connect(dbname="tweets_info", user="gb760")  
cursor = connection.cursor()
connection.commit()
# Fetch result
cursor.execute("SELECT * from Tweets_time_and_text")
record = cursor.fetchall()
df = pd.DataFrame(record)
#print("Result ", df)
cursor.close()
connection.close()

#read tweets in the current minute
cur_m = df.iloc[0,2]
cur_df = df.loc[df[2] == cur_m]
cur_text = df[df.columns[4]]
for i in '!"#$%&()*+-,-./:;<=>?@“”[\\]^_{|}~':
            cur_text = cur_text.replace(i, " ") 
cur_text = str(cur_text)
tot = len (cur_text)
cur_text = set(cur_text.split())
un = len(cur_text)

#Total number of phrases in the prior minute
pri_df = df.loc[df[2] == cur_m-1]
pri_text = df[df.columns[4]]
for j in '!"#$%&()*+-,-./:;<=>?@“”[\\]^_{|}~':
            pri_text = pri_text.replace(j, " ") 
pri_text = str(pri_text)
tot2 = len(pri_text)

pri_text = set(pri_text.split())
un2 = len(pri_text)


#Probability of seeing the phrases in current/prior minute
def Pro(f,v,t):
	p = (1 + f) / (v + t)
	

#trendiness score
import math
def trend(p1, p2):
	if args.word in word_freq:
		tre = math.log10(f1) - math.log10(f2)
		pr = print("The Trendness Score Is:", tre)
		return pr
	else:
        	results1 = print('That word is not in sampled tweets.')
        	return results1
        


# run the main function

if __name__ == '__main__':  

    readtws = process_file()
    word_prob = process_tweets(readtws)
    for w1 in word_prob.values():
    	word_p = w1	
    w2 = 0.9 #random for testing
    volc_p = un 
    word_pr = Pro(w1,un,tot)
    volc_pr = Pro(w2,un2,tot2)
    tre = trend(word_pr,volc_pr)



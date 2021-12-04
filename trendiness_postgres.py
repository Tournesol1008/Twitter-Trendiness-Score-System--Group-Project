#Read Word Input
import argparse
parser = argparse.ArgumentParser(description='Count word frequency')
parser.add_argument('--word', help='Take as input a word or phrase')
args = parser.parse_args() 

#Read the tweets info table from database
from string import punctuation
import psycopg2
import pandas as pd
import connection

#read data from database tweets_info
connection = psycopg2.connect(dbname="tweets_info", user="gb760")  
cursor = connection.cursor()
connection.commit()
# Fetch result
cursor.execute("SELECT * from Tweets_Table")
record = cursor.fetchall()
df = pd.DataFrame(record)
cur_date = df.iloc[-1,0]
cur_hour = df.iloc[-1,1]
cur_min = df.iloc[-1,2]
cur_sec = df.iloc[-1,3]
cur_list = []
pri_list = []

#Compute number of entered words in the current minute
for i in range(len(df)):
    if df.iloc[i,0] == cur_date and df.iloc[i,1] == cur_hour and df.iloc[i,2] == cur_min:
        new_line = df.iloc[i]
        cur_list.append(new_line)
    else:
        pass
cur_df = pd.DataFrame(cur_list)

def process_c_tweets(c_df,phrase):  
    text = ""
    for m in range(len(c_df)):
        text += c_df.iloc[m,4]
    for i in '!"#$%&()*+-,-./:;<=>?@“”[\\]^_{|}~':
        text = text.replace(i, " ") # replace special characters
        text = text.lower() # convert uppercase to lowercase
    count = text.count(phrase)       
    return count
    
#Compute number of entered words in the prior minute
for i in range(len(df)):
    if df.iloc[i,0] == cur_date and df.iloc[i,1] == cur_hour and df.iloc[i,2] == cur_min-1:
        new_line1 = df.iloc[i]
        pri_list.append(new_line1)
    else:
        pass
pri_df = pd.DataFrame(pri_list)

def process_p_tweets(p_df,phrase):  
    text1 = ""
    for n in range(len(p_df)):
        text1 += p_df.iloc[n,4]
    for i in '!"#$%&()*+-,-./:;<=>?@“”[\\]^_{|}~':
        text1 = text1.replace(i, " ") # replace special characters
        text1 = text1.lower() # convert uppercase to lowercase
    count = text1.count(phrase)       
    return count

cursor.close()
connection.close()

#total word in a dataframe
def process_c_un(df3):
	text3 = ""
    for i3 in range(len(df3)):
        text3 += df3.iloc[n,4]
    for j3 in '!"#$%&()*+-,-./:;<=>?@“”[\\]^_{|}~':
        text3 = text3.replace(i, " ") # replace special characters
        text3 = text3.lower() # convert uppercase to lowercase
    t3 = len(text3)     
    return t3

#unique word in the dataframe
def process_c_un(df3):
	text3 = ""
    for i3 in range(len(df3)):
        text3 += df3.iloc[n,4]
    for j3 in '!"#$%&()*+-,-./:;<=>?@“”[\\]^_{|}~':
        text3 = text3.replace(i, " ") # replace special characters
        text3 = text3.lower() # convert uppercase to lowercase
    l3 = set(text3.split())
    u3 = len(l3)     
    return u3



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
        	res = print('That word is not in sampled tweets.')
        	return res
        


# run the main function

if __name__ == '__main__':  

    word_f = process_c_tweets(c_)
    for w1 in word_f.values():
    	word_f = w1	
    w2 = 0.9 #random for testing
    volc_f = un 
    word_pr = Pro(w1,volc_f,tot)
    volc_pr = Pro(w2,word_f,tot2)
    tre = trend(word_pr,volc_pr)



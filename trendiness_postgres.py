#Read Word Input

import argparse
parser = argparse.ArgumentParser(description='Count word frequency')
parser.add_argument('--word', help='Take as input a word or phrase')
args = parser.parse_args() 

#run word count file
import sys 
import os
sys.path.append(os.path.abspath("/home/gb760/Group5-760"))
from word_count import * #use word_count to test
#from word_count_postgres import *
#from vocabulary_size_postgres import *
#run unique word file

#Total number of phrases in the current minute
def tot1():

#Total number of phrases in the prior minute
def tot2():

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
"""
    prior_prob = process_tweets1(readtws)
    for w1 in prior_prob.values():
    	prior_p = w2
"""	
    w2 = 0.9 #random for testing
    volc_p = 20 #random number for testing
    word_pr = pro(w1,v1,t1)
    volc_pr = pro(w2,v2,t2)
    tre = trend(word_pr,volc_pr)



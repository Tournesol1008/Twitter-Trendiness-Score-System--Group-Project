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

#trendiness score
import math
def trend(f1, f2):
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
    word_freq = process_tweets(readtws)
    for w in word_freq.values():
    	word_f = w
    volc_f = 20 #random number for testing
    tre = trend(word_f,volc_f)



#1.Read tweet.txt file
from string import punctuation

def process_file(): 
    try: # open file and handle errors
        f = open("tweets.txt", "r",encoding='utf-8')
    except IOError as s:
        print(s)
        return None
    try: # read file and handle errors
        readtws = f.read()
    except:
        print("Read File Error!")
        return None
    f.close()  
    return readtws
    
#2.Processing the file，count the frequency of each words，and store them in word_freq
def process_tweets(readtws):
    if readtws:
        word_freq = {}
        for i in '!"#$%&()*+-,-./:;<=>?@“”[\\]^_{|}~':
            readtws = readtws.replace(i, " ") # replace special characters
            readtws = readtws.lower() # convert uppercase to lowercase
            words = readtws.split() # split string
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1
        return word_freq

import argparse
parser = argparse.ArgumentParser(description='Count word frequency')
parser.add_argument('--word', help='Take as input a word or phrase')
args = parser.parse_args() 
        
def outputs(word_freq):
    if args.word in word_freq:
        results = print('The word frequency is:', word_freq[args.word])
        return results
    else:
        results1 = print('That word is not in sampled tweets.')
        return results1
        
# run the main function
if __name__ == '__main__':  
    readtws = process_file()
    word_freq = process_tweets(readtws)
    results = outputs(word_freq)

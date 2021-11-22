#1.Read tweet.txt file
from string import punctuation
def process_file(dst): 
    try: # open file and handle errors
        f = open("tweets.txt", "r")
    except IOError as s:
        print(s)
        return None
    try: # read file and handle errors
        bvffer = f.read()
    except:
        print("Read File Error!")
        return None
    f.close()
    return bvffer

#2.Processing the file，count the frequency of each words，and store them in word_freq
def process_buffer(bvffer):
    if bvffer:
        word_freq = {}
        for i in '!"#$%&()*+-,-./:;<=>?@“”[\\]^_{|}~':
            bvffer = bvffer.replace(i, " ") # replace special characters
            bvffer = bvffer.lower() # convert uppercase to lowercase
            words = bvffer.split() # split string
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1
        return word_freq

#3.sorting by frequency，and print out the results
def output_result(word_freq):
    if word_freq:
        sorted_word_freq = sorted(word_freq.items(), key=lambda v: v[1], reverse=True)
        for item in sorted_word_freq[:]:
            print("%s %d " % (item[0], item[1]))

#4.define main function for testing
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('dst')
    args = parser.parse_args()
    dst = args.dst
    bvffer = process_file(dst)
    word_freq = process_buffer(bvffer)
    output_result(word_freq)
    
# 5. run the main function
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('dst')
    args = parser.parse_args()
    dst = args.dst
    bvffer = process_file(dst)
    word_freq = process_buffer(bvffer)
    output_result(word_freq)


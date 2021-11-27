# Group5-760
This is a group project for GB760, which aims to build a system to continuously score phrases and words based on their "trendiness" on Twitter.
## Milestone 1
Milestone 1 contains 6 files: server.py, tweet_json_file.json, tweets.txt, word_count.py, vocabulary_size.py, FAILURE.md. 
In order to run the code, first make sure you are in the right repository, then type in "python <filename>". However, for word_count.py specifically, you need to add "--word <word_or_phrase>" after "python <filename>" in order to count the frequency of the word or phrases you are interested in. 
In terms of the content of those 6 files, server.py serves for reading tweets from the Twitter API as well as writing raw tweets into tweets_json_file.json and writing formated tweets into tweets.txt, while word_count.py and vocabulary_size.py is to compute frequencies of word/phrases and the number of unique word of all the tweets in tweets.txt. Lastly, Failure.md documents points of failure in server.py and recovery logic.

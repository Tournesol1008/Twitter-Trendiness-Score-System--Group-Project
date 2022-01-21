# Group5-760

This is Group5's final project for 2021 Fall Data Technology class, which aims to build a system to continuously score phrases and words based on their "trendiness" on Twitter. The project was be developed on a Linux (Ubuntu 20.04) Virtual Machine.  

## Milestone 1  
  
A. Read tweets from the Twitter API or from _tweet_json_file_(raw tweets generated from API), write cleaned tweets into _tweets.txt_;  
B. Compute frequencies of words and phrases and store the python code in _word_count.py_;  
C. Compute the number of unique words (i.e. the vocabulary size) (_vocabulary_size.py_）;  
D. Document points of failure in server.py, implement code to warn and gracefully recover from such failures (_FAILURE.md_);  

In order to run the code, first make sure you are in the right repository, then type in "<mark>python server.py</mark>", you can add filename after this code by adding "<mark>--filename example.json</mark>". For word_count.py specifically, you need to add "--word <word_or_phrase>" after "python word_count.py" in order to count the frequency of the word or phrases you are interested in.<br />

In terms of the content of those 6 files, server.py serves for reading tweets from the Twitter API as well as writing raw tweets into tweets_json_file.json and writing formated tweets into tweets.txt, while word_count.py and vocabulary_size.py is to compute frequencies of word/phrases and the number of unique word of all the tweets in tweets.txt. Lastly, Failure.md documents points of failure in server.py and recovery logic.<br />

## Milestone 2

Milestone 2 contains 6 files: SCHEMA.md, schema_postgres.sql, server_postgres.py, word_count_postgres.py, vocabulary_size_postgres.py. trendiness_postgres.py.<br />

Firstly, run the "schema_postgres.sql" to create a table named Tweets_Table, this table will be used to save our data read from twitter.<br /> 

Then run the "server_postgres.py" to add tweet date and text content into the table we created previously. You can add specific file after "python server_postgres.py --filename example.json" to read from this file. The json file we created is named <mark>"tweet_json_file.json"</mark>. The default setting will read from Twitter API. After this, you can run <mark>"word_count_postgres.py"</mark> and <mark>"vocabulary_size_postgres.py"</mark> to compute word frequency and the unique words. You can use <mark>"trendiness_postgres.py"</mark> to compute the word's trendiness score at current time.

## Milestone 3

Milestone3 contains 3 files: server_to_kafka.py, server_from_kafka.py, and trendiness_kafka.py. <br />

Firstly, run the "server_to_kafka.py" file to write tweets to a Kafka queue. Then run the "server_from_kafka.py" file to read tweets from Kafka, and save it into a data table. We will use the "trendiness_kafka.py" to compute the trendiness score of each input word. 

Due to the environment set-up issue, even though we are able to run the server_to_kafka.py and server_from_kafka.py, we are not able to see the info from kafka from command line. 





# Group5-760

This is Group5's final project for GB760, which aims to build a system to continuously score phrases and words based on their "trendiness" on Twitter.

## Milestone 1

Milestone 1 contains 6 files: server.py, tweet_json_file.json, tweets.txt, word_count.py, vocabulary_size.py, FAILURE.md.<br />

In order to run the code, first make sure you are in the right repository, then type in "<mark>python server.py</mark>", you can add filename after this code by adding "<mark>--filename example.json</mark>". For word_count.py specifically, you need to add "--word <word_or_phrase>" after "python word_count.py" in order to count the frequency of the word or phrases you are interested in.<br />

In terms of the content of those 6 files, server.py serves for reading tweets from the Twitter API as well as writing raw tweets into tweets_json_file.json and writing formated tweets into tweets.txt, while word_count.py and vocabulary_size.py is to compute frequencies of word/phrases and the number of unique word of all the tweets in tweets.txt. Lastly, Failure.md documents points of failure in server.py and recovery logic.<br />

## Milestone 2

Milestone 2 contains 6 files: SCHEMA.md, schema_postgres.sql, server_postgres.py, word_count_postgres.py, vocabulary_size_postgres.py. trendiness_postgres.py.<br />

Firstly, run the "schema_postgres.sql" to create a table named Tweets_Table, this table will be used to save our data read from twitter.<br /> 

Then run the "server_postgres.py" to add tweet date and text content into the table we created previously. You can add specific file after "python server_postgres.py --filename example.json" to read from this file. The json file we created is named <mark>"tweet_json_file.json"</mark>. The default setting will read from Twitter API. After this, you can run <mark>"word_count_postgres.py"</mark> and <mark>"vocabulary_size_postgres.py"</mark> to compute word frequency and the unique words. You can use <mark>"trendiness_postgres.py"</mark> to compute the word's trendiness score at current time.

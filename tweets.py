a_file = open("tweets.txt", "w")
tweets = []
for i in range(len(results)):
    if results[i]["data"]["lang"] == "en":
        time = str(results[i]["data"]["created_at"][0:10]) + "-" + str(results[i]["data"]["created_at"][11:19].replace(':','-'))
        text = str(results[i]["data"]["text"])
        text = clean_text(text)
        tweet = time + ", " + text
        tweets.append(tweet)
value = "\n".join(tweets)
print(value, file = a_file)
a_file.close()

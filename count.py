#get file object reference to the file
file = open("tweets.txt", "r")

#read content of file to string
data = file.read()

#get number of occurrences of the substring in the string
occurrences = data.count("my")

print('Number of occurrences of the word :', occurrences)

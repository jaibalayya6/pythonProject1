import string

file = open("cloudsecurity.txt", "r")
word_count ={}
print(type(word_count))
for line in file:
 line= line.rstrip()
 words= line.split(" ")
 for word in words:
  for puc in string.punctuation:
    word = word.replace(puc,"")
    word = word.lower()
  if(word in word_count):
   word_count[word] = words.count(word)+1
  else:
   word_count[word] = words.count(word)


for key, value in word_count.items():
   print (f" the word\"{key}\" is repeated {value} times")
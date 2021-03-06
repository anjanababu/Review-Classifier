import re

fo_cleaned = open("cleaned_data.txt","r") 
fo_vocabulary = open("adv_vocabulary.txt","w")
dict_uni = {}
dict_bi = {}

# Unigrams to vocabulary
fo_cleaned = open("cleaned_data.txt","r") 
for line in fo_cleaned:
	words = line.split()
        for word in words[1:]:
	   dict_uni.setdefault(word, 0)
	   dict_uni[word] = dict_uni[word] + 1
	
	for i in range(1,len(words)-1):
		bigram = words[i] + ' ' + words[i+1]
		dict_bi.setdefault(bigram,0)
		dict_bi[bigram] = dict_bi[bigram] + 1

for word in sorted(dict_uni):	
	if(dict_uni[word] >= 1): 	# we have taken every words since we think that would benefit our model
		fo_vocabulary.write(word + "\n")

for word in sorted(dict_bi):	
	if(dict_bi[word] >= 2): 	
		fo_vocabulary.write(word + "\n")

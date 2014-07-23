from __future__ import division
import sys
import json
import re

word_dict={}
def compute_frequencies(tweet_file):
	total=0

	for line in tweet_file:
		tweet_obj = json.loads(line)
		if 'text' in tweet_obj:
			text = re.sub('[^a-zA-Z0-9\n\.]', ' ', tweet_obj['text'])
			words = text.split()

			for word in words:
				total+=1
				word=word.strip()
				if word in word_dict:
					word_dict[word]+=1
				else:
					word_dict[word]=1

	for word in word_dict:		
		word_dict[word]=word_dict[word]/total	
		print word+' '+str(word_dict[word])

def lines(fp):
    print str(len(fp.readlines()))

def main():    
    tweet_file = open(sys.argv[1])
    compute_frequencies(tweet_file)
    # get_all_tweet_sentiments(sent_file,tweet_file)
    # lines(sent_file)
    # lines(tweet_file)

if __name__ == '__main__':
    main()

from collections import Counter
import sys
import json
import re

hashtag_count={}

def get_top_ten(tweet_file):
	for line in tweet_file:
		tweet_obj = json.loads(line)
		if 'entities' in tweet_obj:
			# print tweet_obj['entities']
			# exit()
			if 'hashtags' in tweet_obj['entities']:
				if tweet_obj['entities']['hashtags']:
					if tweet_obj['entities']['hashtags'][0]['text'] in hashtag_count:
						hashtag_count[tweet_obj['entities']['hashtags'][0]['text']]+=1
					else:
						hashtag_count[tweet_obj['entities']['hashtags'][0]['text']]=1

	top_hashtags = dict(Counter(hashtag_count).most_common()[:10])
	for tag in top_hashtags:
		print tag + ' ' + str(top_hashtags[tag])

def lines(fp):
    print str(len(fp.readlines()))

def main():
    # sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[1])    
    get_top_ten(tweet_file)
    # lines(sent_file)
    # lines(tweet_file)

if __name__ == '__main__':
    main()

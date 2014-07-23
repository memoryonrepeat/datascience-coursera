import sys
import json
import re

scores = {} # initialize an empty dictionary

def build_sentiment_dict(sent_file):
	for line in sent_file:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = int(score)  # Convert the score to an integer.

def calculate_sentiment(tweet):
	tweet_obj = json.loads(tweet)
	if 'text' not in tweet_obj:
		return 0
	else:
		text_score=0

		#Remove all special characters using regex"
		text = re.sub('[^a-zA-Z0-9\n\.]', ' ', tweet_obj['text'])

		words = text.split(' ')
		for word in words:
			if word in scores:
				text_score += scores[word]
	return text_score	

def get_all_tweet_sentiments(sent_file,tweet_file):	
	build_sentiment_dict(sent_file)	
	for line in tweet_file:				
		print calculate_sentiment(line)

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    get_all_tweet_sentiments(sent_file,tweet_file)
    # lines(sent_file)
    # lines(tweet_file)

if __name__ == '__main__':
    main()

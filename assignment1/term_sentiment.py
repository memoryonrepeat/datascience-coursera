from __future__ import division
import sys
import json
import re

scores = {} # initialize an empty dictionary

non_sentiment_words = {} #words whose sentiment are yet to be defined

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

		words = text.split()

		#Compute sentence's sentiment score
		for word in words:
			if word in scores:
				text_score += scores[word]

		#Compute not-indexed-words' positive/negative score
		for word in words:
			word=word.strip()
			if word not in scores:
				if word not in non_sentiment_words:
					non_sentiment_words[word]=[1,1,0] #[positive,negative,final]
				else:
					if text_score>0:
						non_sentiment_words[word][0]+=1
					elif text_score<0:
						non_sentiment_words[word][1]+=1
	return text_score	

def get_other_sentiment_scores():
	for word in non_sentiment_words:		
		non_sentiment_words[word][2]=non_sentiment_words[word][0]/non_sentiment_words[word][1]		
		print word + ' ' + str(non_sentiment_words[word][2])


def get_all_tweet_sentiments(sent_file,tweet_file):	
	build_sentiment_dict(sent_file)	
	for line in tweet_file:				
		calculate_sentiment(line)
	get_other_sentiment_scores()

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

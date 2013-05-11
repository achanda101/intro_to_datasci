import sys
import json

def makeAFINNdict():
	afinnfile = open("AFINN-111.txt")
	scores = {} # initialize an empty dictionary
	for line in afinnfile:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = int(score)  # Convert the score to an integer.
	afinnfile.close()
	return scores

def hw(tweet_fp):
    scores = makeAFINNdict()
    # print scores.items() # Print every (term, score) pair in the dictionary
    tweettext_list = [] #Creating an array of dicts, each dict is a tweet
    tweet_sentiment_perline = [] # creating an array of sentiments, one for each tweet
    for line in tweet_fp:
    	tweet = json.loads(line)
    	this_tweet_sen = 0
    	if tweet.has_key("text"):
    		tweettext_list.append(tweet["text"].encode('utf-8'))
    		tweettext = tweet["text"].encode('utf-8')
    		tweettext_words = (tweet["text"].encode('utf-8')).split(" ")
    		for tweet_word in tweettext_words:
    			tweet_word = tweet_word.lower()
    			if scores.has_key(tweet_word):
    				this_tweet_sen += scores[tweet_word]
    		print tweettext
    		print "sentiment: " + str(this_tweet_sen)
    	else:
    		print "-------- tweet has no text --------"

    	tweet_sentiment_perline.append(this_tweet_sen)
    	

   	# print tweet_sentiment_perline
    # print len(tweet_sentiment_perline)
    tweet_fp.seek(0) # reset the filepointer to the beginning of the file


def lines(fp):
    print str(len(fp.readlines()))

def main():
    # sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[1])
    hw(tweet_file)
    # lines(sent_file)
    lines(tweet_file)

if __name__ == '__main__':
    main()

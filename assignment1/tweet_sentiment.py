import sys
import json

def makeAFINNdict(sentiment_fp):
	scores = {} # initialize an empty dictionary
	for line in sentiment_fp:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = int(score)  # Convert the score to an integer.
	return scores

def hw(sent_fp, tweet_fp):
    scores = makeAFINNdict(sent_fp)
    for line in tweet_fp:
    	tweet = json.loads(line)
    	this_tweet_sent = 0
    	if tweet.has_key("text"):
    		# tweettext_list.append(tweet["text"].encode('utf-8'))
    		tweettext = tweet["text"].encode('utf-8')
    		tweettext_words = (tweet["text"].encode('utf-8')).split(" ")
    		for tweet_word in tweettext_words:
    			tweet_word = tweet_word.lower()
    			if scores.has_key(tweet_word):
    				this_tweet_sent += scores[tweet_word]
    		print tweettext
    		print "sentiment: " + str(this_tweet_sent)
    	else:
    		print "sentiment: 0"

def lines(fp):
    print str(len(fp.readlines()))

def main():
	sent_file  = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	hw(sent_file, tweet_file)
	sent_file.seek(0) # reset the filepointer to the beginning of the file
	tweet_file.seek(0)
	lines(sent_file)
	lines(tweet_file)
	sent_file.close()
	tweet_file.close()
                                  
if __name__ == '__main__':
    main()

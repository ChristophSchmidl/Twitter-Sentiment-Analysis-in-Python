import sys
import json
import pprint

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))
    fp.seek(0) # returns the cursor of the file to the beginning

def getContent(fp):
    print fp.read()


def computeSentiment(wordList, scoreList):
    score = 0
    for word in wordList:
        if word in scoreList:
            score += scoreList[word]

    return score


def preprocessTweet(tweet):
    punc = (",./;'?&-#!@")

    splitList = []
    stripedList = []

    if "text" in tweet:
        splitList = str.split((tweet['text'].encode('ascii', 'replace')).lower().translate(None, punc))

    for item in splitList:
        stripedList.append(item.strip())

    return stripedList


def computeAllSentiments(tweets, scoreList):

    sentiments = []

    for tweet in tweets:
        sentiments.append(computeSentiment(preprocessTweet(tweet), scoreList))

    return sentiments


def main():

    #json.loads(sys.argv[2])

    sent_file = open(sys.argv[1], 'r')
    tweet_file = open(sys.argv[2], 'r')
    #lines(sent_file)
    #lines(tweet_file)

    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    #print scores.items() # Print every (term, score) pair in the dictionary
    sent_file.seek(0)

    tweets = []

    with tweet_file as f:
        for line_str in f:
            tweets.append(json.loads(line_str))

    #print "number of sentimentscores" + str(len(computeAllSentiments(tweets, scores)))

    sentimentScores = computeAllSentiments(tweets, scores)

    for item in sentimentScores:
        print item
    #tweetDatastructure = json.loads(tweet_file.read())


if __name__ == '__main__':
    main()

__author__ = 'cs'

import sys
import json

def load_and_get_tweetfile(tweet_file):
    tweets = []

    with tweet_file as f:
        for line_str in f:
            tweets.append(json.loads(line_str))

    return tweets


def preprocess_tweet(tweet):
    punc = (",./;'?&-#!@")

    splitList = []
    stripedList = []

    if "text" in tweet:
        splitList = str.split((tweet['text'].encode('ascii', 'replace')).lower().translate(None, punc))

    for item in splitList:
        stripedList.append(item.strip())

    return stripedList


def get_preprocessed_tweet_list(tweets):
    tweetList = []

    for tweet in tweets:
        tweetList.append(preprocess_tweet(tweet))

    #print str(len(tweetList))
    return tweetList


def get_term_count_dict(tweets):

    result = {}

    for tweet in tweets:
        for term in tweet:
            if term in result:
                result[term] += 1
            else:
                result[term] = 1
    return result


def main():

    tweets = load_and_get_tweetfile(open(sys.argv[1]))


    tweet_text_list = get_preprocessed_tweet_list(tweets)


    terms =  get_term_count_dict(tweet_text_list)

    overall_term_count = sum(terms.values())
    #print overall_term_count
    for term in terms:
       print term + " " + str(float(terms[term]) / overall_term_count)








if __name__ == '__main__':
    main()
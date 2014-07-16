__author__ = 'cs'

import sys
import json
from operator import itemgetter

def load_and_get_tweetfile(tweet_file):
    tweets = []

    with tweet_file as f:
        for line_str in f:
            tweets.append(json.loads(line_str))

    return tweets


def preprocess_tweet(tweet):

    hashlist = []

    if "entities" in tweet:
        ent = tweet['entities']
        if "hashtags" in ent and len(ent['hashtags']) != 0:
            for item in ent["hashtags"]:
                hashlist.append(item['text'])
            return hashlist

    return []


def get_hashtag_dict(tweets):
    hash_dict = {}

    for tweet in tweets:
        hash_list = preprocess_tweet(tweet)
        if len(hash_list) != 0:
            for hashe in hash_list:
                if hashe in hash_dict:
                    hash_dict[hashe] += 1
                else:
                    hash_dict[hashe] = 1

    return hash_dict


def get_term_count_dict(tweets):

    result = {}

    for tweet in tweets:
        for term in tweet:
            if term in result:
                result[term] += 1
            else:
                result[term] = 1
    return result



def get_top_ten_hashtags(hash_dict):

    top_ten = sorted(hash_dict.items(), key=itemgetter(1), reverse=True)[1:11]

    return top_ten



def main():

    tweets = load_and_get_tweetfile(open(sys.argv[1]))




    hash_dict = get_hashtag_dict(tweets)


    topten = get_top_ten_hashtags(hash_dict)

    for item in topten:
        print item[0] + " " + str(item[1])

    #terms = get_term_count_dict(tweet_text_list)

    #print get_top_ten_hashtags(terms)



if __name__ == '__main__':
    main()
__author__ = 'cs'


import sys
import json
import types


def load_and_get_scorefile(sent_file):
    scores = {}
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    #print scores.items() # Print every (term, score) pair in the dictionary
    sent_file.seek(0)

    return scores

def load_and_get_tweetfile(tweet_file):
    tweets = []

    with tweet_file as f:
        for line_str in f:
            tweets.append(json.loads(line_str))

    return tweets


def main():

    scores = load_and_get_scorefile(open(sys.argv[1]))
    tweets = load_and_get_tweetfile(open(sys.argv[2]))

    state_scores = {}

    for tweet in tweets:
        sentiment = 0
        if 'text' in tweet:
            terms = tweet['text'].lower().encode('utf-8').split()
            for term in terms:
                if term in scores:
                    sentiment = sentiment + scores[term]
        if 'place' in tweet and type(tweet['place']) is not types.NoneType:
            if 'full_name' in tweet['place'] and type(tweet['place']['full_name']) is not types.NoneType:
                if 'country_code' in tweet['place'] and type(tweet['place']['country']) is not types.NoneType:
                    if tweet['place']['country'] == 'United States':
                        name_line = tweet['place']['full_name'].encode('utf-8')
                        details = name_line.split()
                        state = details[-1]
                        if len(state) == 2:
                            if state_scores.has_key(state):
                                state_scores[state] = state_scores[state] + sentiment
                            else:
                                state_scores[state] = sentiment

    happiest_state = state_scores.keys()[0]
    for state in state_scores:
        if state_scores[state] > state_scores[happiest_state]:
            happiest_state = state
    print happiest_state


if __name__ == '__main__':
    main()
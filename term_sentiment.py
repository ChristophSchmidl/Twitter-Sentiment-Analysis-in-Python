import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))


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


def load_and_get_scorefile(sent_file):
    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    #print scores.items() # Print every (term, score) pair in the dictionary
    sent_file.seek(0)

    return scores




def get_unknown_words_dict(tweet_list, score_list):

    unknown_words = {}

    for tweet in tweet_list:
        unknown = get_unknown_words_in_tweet(tweet, score_list)

        if len(unknown) != 0:
            for term in unknown:
                unknown_words[str(term)] = 0

    return unknown_words



def computeSentiments(unknown_words_dict, tweet_list, score_list):


    counter = 0
    for unknown in unknown_words_dict:
        #if counter == 100:
            #break
        counter += 1
        for tweet in tweet_list:
            known_words = get_known_words_in_tweet(tweet, score_list)
            if str(unknown) in tweet and len(known_words) != 0:
                score = 0
                for known in known_words:
                    score += score_list[known]
                unknown_words_dict[unknown] = score
                break

    return unknown_words_dict







def get_unknown_words_in_tweet(tweet, score):

    unknown = []

    for term in tweet:
        if str(term) not in score:
            unknown.append(term)

    return unknown



def get_known_words_in_tweet(tweet, score):

    known = []

    for term in tweet:
        if str(term) in score:
            known.append(term)

    return known



def return_lists_with_word(word_list, search_term):

    resultList = []

    for i in range(0, len(word_list)):
        if search_term in word_list[i]:
            resultList.append(word_list[i])

    return resultList




def load_and_get_tweetfile(tweet_file):
    tweets = []

    with tweet_file as f:
        for line_str in f:
            tweets.append(json.loads(line_str))

    return tweets




def main():

    scores = load_and_get_scorefile(open(sys.argv[1]))
    tweets = load_and_get_tweetfile(open(sys.argv[2]))


    tweet_text_list = get_preprocessed_tweet_list(tweets)




    #for tweet in tweet_text_list:
      #  print get_known_words_in_tweet(tweet, scores)


   # print get_known_words_in_tweet(tweet_text_list[10], scores)

    unknown_words = get_unknown_words_dict(tweet_text_list, scores)

    sentiments = computeSentiments(unknown_words, tweet_text_list, scores)


    for sent in sentiments:
        print str(sent) + " " + str(sentiments[sent])

    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()

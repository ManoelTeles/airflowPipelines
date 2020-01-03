import pandas as pd
import GetOldTweets3 as got


def main():
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('kimetsu no yaiba')\
                                           .setSince("2019-05-01")\
                                           .setUntil("2019-11-30")\
                                           .setMaxTweets(10)
    tweet = got.manager.TweetManager.getTweets(tweetCriteria)

    obj_tweets = []
    for t in tweet:
        element_tweet = {}
        element_tweet["id"] = t.id
        element_tweet["date"] = t.date
        element_tweet["text"] = t.text
        obj_tweets.append(element_tweet)

    df = pd.DataFrame(obj_tweets)
    df.to_csv('/tmp/tweets.csv', sep=';', index=False)

if __name__ == '__main__':
    main()




































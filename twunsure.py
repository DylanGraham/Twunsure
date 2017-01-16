import tweepy
import secrets

auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
auth.set_access_token(secrets.access_token, secrets.access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('ducks')
for tweet in public_tweets:
    print(tweet.text)

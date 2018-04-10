# Dependencies
import tweepy
import json
import time

# Twitter API Keys
consumer_key = "TxWqhV1iSJUMQM7vtoGWEx1jZ"
consumer_secret = "aO8ov92ktffAUjVSbJkbDQ4O5fWhoZ02YhrIjGN4ilaCClK75u"
access_token = "4876379418-s3LnanUre5v4FycRGho3ABsfQoupCwvG6Y1YYex"
access_token_secret = "fIS72sjmhsIJ0d7jZO15gzREbBK0iU71UcfcYrJc663vP"


# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
def TweetOut(tweet_number):
    api.update_status(
        "Can't stop. Won't stop. Chatting! This is Tweet #%s!" %
        tweet_number)

# Create a function that calls the TweetOut function every minute
counter = 0

# Infinite loop
while(True):

    # Call the TweetQuotes function and specify the tweet number
    TweetOut(counter)

    # Once tweeted, wait 60 seconds before doing anything else
    time.sleep(60)

    # Add 1 to the counter prior to re-running the loop
    counter = counter + 1

# New comment
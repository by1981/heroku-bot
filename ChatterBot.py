# Dependencies
import tweepy
import json
import time

# Twitter API Keys
consumer_key = "ImLGT5Pbebk33jYv76ozNt5KB"
consumer_secret = "alFm0kHzJ3IFhDlNn5Z4ifX4JpzANpqxFgWxHbs4Ewv2kwd8tc"
access_token = "4876379418-qNp9F4td5lyyefVcE3Q7eNNNiJtFDTClHncUuRt"
access_token_secret = "tZA2bgIXF7OzNzPLMJImYvJ5AQ90cLkPYLsdPRP3bBnNC"


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
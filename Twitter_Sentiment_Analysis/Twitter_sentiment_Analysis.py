
import tweepy
from Textblob import Textblob

# Step 1 - Authenticate
consumer_key = '7K7lkqYPyOqIxLbeSzZGKre6T'
consumer_secret = 'L3mJl2k1nFI7Q9BZTccRx8TWdGf629QzvI2nvuP70EboI2Ql3X'

access_token = '590442657-WwdOZ7VUE8GIWg7C5KoJPvYNu5710exmZPa1hT8r'
access_token_secret = 'uIk6ZxD962WLFdhVoofoRpiskeswvXHachfpH6vQNiFgA'


auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)


#Step 2 - Retrieve Tweets
public_tweets = api.search('Modi')

for tweet in public_tweets:
	print(tweet.text)


	#Step 3 Perform Sentiment Analysis on Tweets
	analysis = textblob(tweet.text)
	print(analysis.sentiment)
	print("")
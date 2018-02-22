from twython import Twython, TwythonError
from io import BytesIO
import requests
import os



consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

twitter = Twython(
	consumer_key,
	consumer_secret,
	access_token,
	access_token_secret
)


def write_tweet_only(tweet):
	try:
		twitter.update_status(status=tweet)
		print("Tweeted : {}".format(tweet))
		return True
	except TwythonError as e:
		print(e)
		return False

def write_tweet_url(tweet, url):
	response = requests.get(url)
	photo = BytesIO(response.content)
	response = twitter.upload_media(media=photo)
	try:
		twitter.update_status(status=tweet, media_ids=[response['media_id']])
		print("Tweeted with image: {}".format(tweet))
		return True
	except TwythonError as e:
		print(e)
		return False


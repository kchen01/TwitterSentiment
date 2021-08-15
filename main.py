import re
from collections import defaultdict
from codes import apikey, url
from twitterAPI import get_tweets
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import sys

# get username
username = str(sys.argv[1])
print("Retrieving tweets for " + username + " for analysis...")

# build query and get relevant tweets
query = f"to:{username} -is:retweet"

r = get_tweets(query=query)

# try:   
#     r = get_tweets(query=query)
# except Exception as e:
#     print("There was an issue with your input. Please check that you spelled the username properly and that the user is a public account.")
#     quit()
  
# regex for removing unwanted characters 
mentions = re.compile('@\S+')
links = re.compile('http\S+')
hashtags = re.compile('#\S+')
spaces = re.compile('\s{2,}')

texts = []
for index, item in enumerate(r):
    text = item
    text = text.replace('RT ', '')
    text = re.sub(mentions, '', text)
    text = re.sub(links, '', text)
    text = re.sub(hashtags, '', text)
    text = re.sub(spaces, ' ', text)
    text = text.strip()
    if len(text) > 0:
        print(text)
        texts.append(text)

print("______________________________________________________ \n")

# create tone analyzer instance
authenticator = IAMAuthenticator(apikey)
ta = ToneAnalyzerV3(version='2017-09-21', authenticator=authenticator)
ta.set_service_url(url)

# analyzes tones and stores them in a dictionary
feelings = defaultdict(lambda: 0)
total = 0
text = '\n'.join(texts)
res = ta.tone(text).get_result()
for sentence in res["sentences_tone"]:
    for tone in sentence["tones"]:
        feelings[tone["tone_name"]] += tone["score"]
        total += tone["score"]

# converts all tones into a proportion
for key in feelings:
    feelings[key] /= total

# output
for key in feelings:
    print(f"{key} was {int(feelings[key] * 100)}% of Twitter users' recent reactions to {username}." )
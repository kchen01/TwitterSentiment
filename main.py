import re
from collections import defaultdict
from codes import apikey, url
from twitterAPI import get_tweets

mentions = re.compile('@\S+')
links = re.compile('http\S+')
hashtags = re.compile('#\S+')
spaces = re.compile('\s{2,}')
#name = input()
name = 'tedcruz'
query = f"to:{name}"
r = get_tweets(query=query)

texts = []
for index, item in enumerate(r):
    #print(index)
    text = item
    # print(f'{index}: {text}')
    text = text.replace('RT ', '')
    text = re.sub(mentions, '', text)
    text = re.sub(links, '', text)
    text = re.sub(hashtags, '', text)
    text = re.sub(spaces, ' ', text)
    text = text.strip()
    if len(text) > 0:
        print(text)
        texts.append(text)

from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json

authenticator = IAMAuthenticator(apikey)
ta = ToneAnalyzerV3(version='2017-09-21', authenticator=authenticator)
ta.set_service_url(url)

feelings = defaultdict(lambda: 0)
total = 0
text = '\n'.join(texts)
res = ta.tone(text).get_result()
# print(json.dumps(res, indent=4))
for sentence in res["sentences_tone"]:
    for tone in sentence["tones"]:
        #print(f'{tone["tone_name"]} with a score of {tone["score"]}')
        feelings[tone["tone_name"]] += tone["score"]
        total += tone["score"]

print("total: ", total)

for key in feelings:
    feelings[key] /= total

for key in feelings:
    print(f"{key} was {int(feelings[key] * 100)}% of people's recent reactions to {name}." )
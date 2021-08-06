from time import process_time
import re
from collections import defaultdict
from TwitterAPI import TwitterAPI
import json
from codes import consumer_key, consumer_secret, access_token_key, access_token_secret
api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

mentions = re.compile('@\S+')
links = re.compile('http\S+')
hashtags = re.compile('#\S+')
spaces = re.compile('\s{2,}')
#name = input()
name = "taylorswift13"
r = api.request('search/tweets', {'q': f'to:{name}'})

texts = []
for index, item in enumerate(r):
    #print(index)
    text = item["text"]
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

apikey = 'Ufh0HLmiJsrRftdDNLxKX-Y4wsk1529Kqy5Rz4I5wma1'
url = 'https://api.us-south.tone-analyzer.watson.cloud.ibm.com/instances/fe6c2f19-6c9b-4406-a09b-abb62fd53f65'

from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json

authenticator = IAMAuthenticator(apikey)
ta = ToneAnalyzerV3(version='2017-09-21', authenticator=authenticator)
ta.set_service_url(url)

feelings = defaultdict(lambda: 0)
total = 0
for text in texts:
    res = ta.tone(text).get_result()

    for tone in res["document_tone"]["tones"]:
        #print(f'{tone["tone_name"]} with a score of {tone["score"]}')
        feelings[tone["tone_name"]] += tone["score"]
        total += tone["score"]

print("total: ", total)

for key in feelings:
    feelings[key] /= total

for key in feelings:
    print(f"{key} was {int(feelings[key] * 100)}% of people's recent reactions to {name}." )



    
import json
from codes import token
import requests

def auth():
    return token

def create_headers(bearer_token):
    headers = {"Authorization":  f"Bearer {bearer_token}"}
    return headers

def create_url(keyword):
    search_url = f"https://api.twitter.com/2/tweets/search/recent?query={keyword}"
    return (search_url)


def connect_to_endpoint(url, headers, params={}, next_token = None):
    params['next_token'] = next_token   #params object received from create_url function
    response = requests.request("GET", url, headers = headers, params=params)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def get_tweets(query='to:taylorswift13'):
    bearer_token = auth()
    headers = create_headers(bearer_token)
    url = create_url(query)
    data = []
    json_response = connect_to_endpoint(url, headers)

    next_token = json_response['meta']['next_token']

    while next_token and len(data) < 100:
        for tweet in json_response["data"]:
            data.append(tweet['text'])
        json_response = connect_to_endpoint(url, headers, next_token=next_token)

        try:
            next_token = json_response['meta']['next_token']
        except KeyError:
            return data

    return data
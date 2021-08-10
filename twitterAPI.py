from codes import token
import requests
import json

def auth():
    return token

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def create_url(keyword):
    
    search_url = "https://api.twitter.com/2/tweets/search/all" #Change to the endpoint you want to collect data from

    #change params based on the endpoint you are using
    query_params = {'query': keyword,
                    'tweet.fields': 'id,text,author_id,in_reply_to_user_id,conversation_id,created_at,lang,public_metrics,referenced_tweets,source',
                    'user.fields': 'id,name,username,created_at,description,public_metrics,verified',
                    'next_token': {}
                }
    return (search_url, query_params)


def connect_to_endpoint(url, headers, params, next_token = None):
    params['next_token'] = next_token   #params object received from create_url function
    response = requests.request("GET", url, headers = headers, params = params)
    print("Endpoint Response Code: " + str(response.status_code))
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

if __name__ == '__main__':
    name = 'taylorswift13'
    bearer_token = auth()
    headers = create_headers(bearer_token)
    keyword = f'to:{name}'
    url = create_url(keyword)
    json_response = connect_to_endpoint(url[0], headers, url[1])
    print(json.dumps(json_response, indent=4, sort_keys=True))
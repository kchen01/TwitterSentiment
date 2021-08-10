apikey = 'Ufh0HLmiJsrRftdDNLxKX-Y4wsk1529Kqy5Rz4I5wma1'
url = 'https://api.us-south.tone-analyzer.watson.cloud.ibm.com/instances/fe6c2f19-6c9b-4406-a09b-abb62fd53f65'

from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator(apikey)
ta = ToneAnalyzerV3(version='2017-09-21', authenticator=authenticator)
ta.set_service_url(url)

res = ta.tone('I cried watching YOU. I feel so lucky to have gotten to watch you all these years, but this week was a lesson in emotional intelligence and resilience. We all learned from you. Thank you.').get_result()

for tone in res["document_tone"]["tones"]:
    print(f'{tone["tone_name"]} with a score of {tone["score"]}')
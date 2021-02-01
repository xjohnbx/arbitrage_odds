# This is a python program to calculate arbitrage betting opportunities

import json
import requests
from pprint import pprint

#sports_response = requests.get('https://api.the-odds-api.com/v3/sports', params={
#	'api_key': api_key
#})
#
#sports_json = json.loads(sports_response.text)
#
#if not sports_json['success']:
#	print('There was a problem with the sports request:', sports_json['msg'])


sport_key = 'upcoming'

odds_response = requests.get('https://api.the-odds-api.com/v3/odds', params={
									'api_key': api_key,
									'sport': sport_key,
									'region': 'us'
							  })
							  
odds_json = json.loads(odds_response.text)
if not odds_json['success']:
	print('There was a problem with the odds request:', odds_json['msg'])
	
else:
	pprint(odds_json)
	
	print('Remaining requests', odds_response.headers['x-requests-remaining'])
	print('Used requests', odds_response.headers['x-requests-used'])

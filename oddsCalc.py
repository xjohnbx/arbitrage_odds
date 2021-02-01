# This is a python program to calculate arbitrage betting opportunities

import json
import requests
from oddsClass import Data
from pprint import pprint

api_key = # You will need an API key to run

sport_key = 'basketball_nba'

data = ''

def main():
	getData()
	checkOdds()
	
def getData():
	global data
	odds_response = requests.get('https://api.the-odds-api.com/v3/odds', params={
									'api_key': api_key,
									'sport': sport_key,
									'region': 'us'
							  })

	odds_json = json.loads(odds_response.text)
	pprint(odds_json)
	data = Data(**odds_json)

	if data.success:
		print("Successful class implementation")

	if not odds_json['success']:
		print('There was a problem with the odds request:', odds_json['msg'])

	else:
		print('Remaining requests', odds_response.headers['x-requests-remaining'])
		print('Used requests', odds_response.headers['x-requests-used'])

def checkOdds():
	games = data.data
	
	for game in games:
		dkOdds = []
		fdOdds = []
		for site in game.sites:
			if site.site_key == 'draftkings':
				dkOdds = site.odds.h2h
			elif site.site_key == 'fanduel':
				fdOdds = site.odds.h2h
		
		if len(dkOdds) > 1 and len(fdOdds) > 1:
			homeTeamSportsbook = 'draftkings' if dkOdds[0] > fdOdds[0] else 'fanduel'
			awayTeamSportsbook = 'draftkings' if dkOdds[1] > fdOdds[1] else 'fanduel'
			
			homeTeamOdds = dkOdds[0] if dkOdds[0] > fdOdds[0] else fdOdds[0]
			awayTeamOdds = dkOdds[1] if dkOdds[1] > fdOdds[1] else fdOdds[1]

			yesOrNo = canBeArbitrageBet(homeTeamOdds, awayTeamOdds)
			print(yesOrNo)
			if yesOrNo:
				print("Game: {}\n_________________________\nHome Team: {} - {}\nAway Team: {} - {}\n\n".format(game.home_team, homeTeamSportsbook, homeTeamOdds, awayTeamSportsbook, awayTeamOdds))

def canBeArbitrageBet(homeOdds, awayOdds):
	return True if ((1/homeOdds) + (1/awayOdds)) * 100 < 100 else False

main()


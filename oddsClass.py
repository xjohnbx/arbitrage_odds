# Python file containing classes

class Data():
	def __init__(self, success, data=None):
		if data is not None:
			dataCollection = []
			for game in data:
				dataCollection.append(Game(**game))
			self.data = dataCollection
		
		self.success = success
			
class Game():
	def __init__(self, commence_time, home_team, sites, sites_count, sport_key, sport_nice, teams):
		self.commence_time = commence_time
		self.home_team	= home_team
		
		siteCollection = []
		for site in sites:
			siteCollection.append(Site(**site))
		self.sites = siteCollection
		
		self.site_count = sites_count
		self.sport_key = sport_key
		self.sport_nice = sport_nice
		self.teams = teams
		
		
class Odds():
	def __init__(self, h2h, h2h_lay=None):
		self.h2h = h2h # Note: h2h is an arary of odds - HomeTeam first then AwayTeam
		self.h2h_lay = h2h_lay
		
class Site():
	def __init__(self, last_update, odds, site_key, site_nice):
		self.last_update = last_update
		self.odds = Odds(**odds)
		self.site_key = site_key
		self.site_nice = site_nice

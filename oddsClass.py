# Python file containing classes

class Data():
	def __init__(self, success, data=None):
		if data is not None:
			dataCollection = []
			for event in data:
				dataCollection.append(Event(**event))
		
		self.success = success
			
class Event():
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
	def __init__(self, h2h):
		self.h2h = h2h
		
class Site():
	def __init__(self, last_update, odds, site_key, site_nice):
		self.last_update = last_update
		self.odds = Odds(**odds)
		self.site_key = site_key
		self.site_nice = site_nice
		
		

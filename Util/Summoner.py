import util
import urllib2
import json
import url

BASE_URL = url.get_summoner_name_url()

class Summoner:

	def __init__(self, summonerId, name, profileIconId, revisionDate, summonerLevel):
		self.summonerId = summonerId
		self.name = name
		self.profileIconId = profileIconId
		self.revisionDate = revisionDate
		self.summonerLevel = summonerLevel

	def print_self(self):
		util.log(str(self.summonerId) + " " + self.name)

def writeToFile(summoner):
	util.log(summoner)

def parseJson(data, name):
	jsonData = json.loads(data)
	#util.log(jsonData)

	myId = jsonData["id"]
	myName = jsonData["name"]
	myProfileIconId = jsonData["profileIconId"]
	myRevisonDate = jsonData["revisionDate"]
	mySummonerLevel = jsonData["summonerLevel"]

	summoner = Summoner(myId, myName, myProfileIconId, myRevisonDate, mySummonerLevel)
	#util.log(summoner.summonerId)
	#util.log(summoner.name)
	return summoner

def getSummonerByName(region, name):

	name = util.replace(name, " ", "")

	ApiKey = util.getApiKey()
	url = BASE_URL
	url = util.replace(url, "{region}", region)
	url = util.replace(url, "{summoner_name}", name)
	url = util.replace(url, "{api_key}", ApiKey)
	url = util.replace(url, "{version}", util.getSummonerVersion())
	#util.log(url)

	summonerFound = False

	try:
		response = urllib2.urlopen(url)
		data = response.read()
		summoner = parseJson(data, name)
		summonerFound = True
		return summoner
	except:
		util.log("Summoner not Found")



sum = getSummonerByName("na1", "vinay")
sum.print_self()

SUMMONER_NAME_URL = "https://{region}.api.riotgames.com/lol/summoner/{version}/summoners/by-name/{summoner_name}?api_key={api_key}"
LEAUGE_URL = "https://{region}.api.riotgames.com/lol/league/{version}/leagues/by-summoner/{summoner_id}?api_key={api_key}"


def getSummonerNameUrl():
    return SUMMONER_NAME_URL

def getLeagueUrl():
    return LEAUGE_URL
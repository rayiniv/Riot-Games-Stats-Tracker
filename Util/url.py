SUMMONER_NAME_URL = "https://{region}.api.riotgames.com/lol/summoner/{version}/summoners/by-name/{summoner_name}?api_key={api_key}"


def get_summoner_name_url():
    return SUMMONER_NAME_URL
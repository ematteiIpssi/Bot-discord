import os
from riotwatcher import LolWatcher, ApiError
from dotenv import load_dotenv
load_dotenv()

RIOT_KEY = os.getenv('RIOT_KEY')

lol_watcher = LolWatcher(RIOT_KEY)
# def rankStat():
#     me =myAccount()
#     return lol_watcher.league.by_summoner(my_region, me['id'])
   
def patch():
    versions = lol_watcher.data_dragon.versions_for_region("euw1")
    return versions['n']['champion']

def champion():
    return lol_watcher.data_dragon.champions(patch())
    

# For Riot's API, the 404 status code indicates that the requested data wasn't found and
# should be expected to occur in normal operation, as in the case of a an
# invalid summoner name, match ID, etc.
#
# The 429 status code indicates that the user has sent too many requests
# in a given amount of time ("rate limiting").

try:
    response = lol_watcher.summoner.by_name('euw1', 'this_is_probably_not_anyones_summoner_name')
except ApiError as err:
    if err.response.status_code == 429:
        print('We should retry in {} seconds.'.format(err.headers['Retry-After']))
        print('this retry-after is handled by default by the RiotWatcher library')
        print('future requests wait until the retry-after time passes')
    elif err.response.status_code == 404:
        print('Summoner with that ridiculous name not found.')
    else:
        raise

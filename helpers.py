# Get the temperature and weather information for your current location (worldwide) from Weather Underground's API
# insert the latitude and longitude of your current location into Weather Underground's API
# Weather Underground's API documentation: https://www.wunderground.com/weather/api/d/docs?d=data/conditions&MR=1
# Example: http://api.wunderground.com/api/9af690c1b08dcb17/conditions/q/42.36800751795526,-71.11559132022597.json

import urllib.request, json

def geo(latitude, longitude):
    key = "9af690c1b08dcb17"
    # source code: https://stackoverflow.com/questions/12934699/selecting-fields-from-json-output
    f = urllib.request.urlopen(f"http://api.wunderground.com/api/{key}/conditions/q/{latitude},{longitude}.json")
    values = json.load(f)
    f.close()
    return(values['current_observation'])


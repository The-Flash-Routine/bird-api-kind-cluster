import requests
from . import parser as parserMod

weatherApiDomain = "api.weather.gov"

def getWeather(state: str):
    # Initialize
    weather = []
    # Fetch raw response from weather API
    weatherResponse = requests.get(f'https://{weatherApiDomain}/alerts/active?area={state}')
    # Check if a valid state code was provided by response code
        # If response code was 200 then parse and return result
        # If response code was not 200 then provide a custom message
    if weatherResponse.status_code == 200:
        weatherResponseBody = weatherResponse.json()
        for item in weatherResponseBody["features"]:
            weather.append(parserMod.constructWeatherInformationData(item))

    if len(weather) == 0:
        weather.append(parserMod.constructDefaultWeather())

    return weather
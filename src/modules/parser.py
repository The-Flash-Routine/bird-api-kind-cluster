# Method to construct Bird Data by picking certain fields
def constructBirdInformationData(birdData):
    return {
        "name": birdData["bird"],
        "scientificName": birdData["scientific_name"],
    }

# Method to construct default message fpr Weather Data
def constructDefaultWeather():
    return {"description": "No weather alert available for provided state code"}

# Method to construct Weather Data by picking certain fields
def constructWeatherInformationData(weatherAlert):
    return {
        "messageType": weatherAlert["properties"]["messageType"],
        "instruction": weatherAlert["properties"]["instruction"],
        "severity": weatherAlert["properties"]["severity"],
        "certainty": weatherAlert["properties"]["certainty"],
        "urgency": weatherAlert["properties"]["urgency"],
        "description": weatherAlert["properties"]["description"]
    }
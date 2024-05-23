from flask import Flask
from modules import weather as weatherMod ,bird as birdMod
import os

app = Flask(__name__)

# Exposing introduction API
@app.route('/', methods=['GET'])
def hello():
    return "Add a 2 letter state param to learn about birds and the weather challenges they face.", \
           200, \
           {'Content-Type': 'text/html; charset=utf-8'}

# Exposing get Bird information API
@app.route('/<state>',methods=['GET'])
def bird(state):
    # Fetching Bird Data
    birdData = birdMod.getBird(state)

    # Fetching Weather Data
    weatherData = weatherMod.getWeather(state)
    out = {
        "stateCodeAbbrevation": state,
        "data": {
            "birds": birdData, 
            "weather": weatherData
        }
    }
    return out, 200, {'Content-Type': 'application/json'}


if __name__ == '__main__':
      app.run(host="0.0.0.0",port=os.environ['APP_PORT'])

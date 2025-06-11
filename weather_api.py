import requests
API_KEY = '4ca5ac683f50b267fd6a25b6ff39741e'

def get_weather(in_lat='64.7502', in_long='20.9509'):

    lat = in_lat
    lon = in_long

    respond = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}')
    json_content = respond.json()

    weather_concat = f'{json_content["city"]["name"]}, {json_content["list"][0]["dt_txt"]}, {json_content["list"][0]["main"]["temp"]}, {json_content["list"][0]["weather"][0]["description"]} \n'
    return weather_concat

import requests


def get_weather(city):
    url = "https://wttr.in/{}?M?qnTqu&lang=ru".format(city)
    response = requests.get(url)
    response.raise_for_status()
    print(response.text)


get_weather("Лондон")
get_weather("Шереметьево")
get_weather("Череповец")

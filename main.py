import requests


def get_weather(city):
    url = "https://wttr.in/{}".format(city)
    payload = {"MqnT": "", "lang": "ru"}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.text


def main():
    locations = ["Лондон", "SVO", "Череповец"]
    for location in locations:
        print(get_weather(location))


if __name__ == "__main__":
    main()

import requests


def get_weather(city):
    url = "https://wttr.in/{}".format(city)
    payload = {"MqnTqu": "", "lang": "ru"}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    print(response.text)


def main():
    get_weather("Лондон")
    get_weather("Шереметьево")
    get_weather("Череповец")


if __name__ == "__main__":
    main()

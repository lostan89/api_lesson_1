import requests

url = "https://wttr.in/{}?M?qnTqu&lang=ru".format("Лондон")
response = requests.get(url)
response.raise_for_status()
print(response.text)
url = "https://wttr.in/{}?M?qnTqu&lang=ru".format("Шереметьево")
response = requests.get(url)
response.raise_for_status()
print(response.text)
url = "https://wttr.in/{}?M?qnTqu&lang=ru".format("Череповец")
response = requests.get(url)
response.raise_for_status()
print(response.text)

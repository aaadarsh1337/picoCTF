import requests

while True:
    response = requests.get('http://mysterious-sea.picoctf.net:56618/')
    if "No flag in this service" not in response.text:
        print(respone.text)

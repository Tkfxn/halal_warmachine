import requests
import hmac
import hashlib
import time
import urllib.parse

# Replace these with your actual API key and secret from Binance
api_key = "CueL87oLc7bJXTrzOIhu9EagkWY7ThhXlX6UkzQ96JYcExEYmOhd7dooHw6HeHwC"
secret_key = "DG8S1PRbdLPHTkuevY92qsB4DzPHZIaFOzYQiEZp3l0HCIOt2RM6ZmdTPkHUdPMM"

base_url = "https://api.binance.com"
path = "/api/v3/account"

timestamp = round(time.time()*1000)

params = {
    "timestamp": timestamp
}

querystring = urllib.parse.urlencode(params)
signature = hmac.new(secret_key.encode('utf-8'), msg=querystring.encode('utf-8'), digestmod=hashlib.sha256).hexdigest()

url = base_url + path + '?' + querystring + '&signature=' + signature
print(url)

payload = {}
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-MBX-APIKEY': api_key
}

response = requests.request("GET", url, headers=headers, data=payload)
result = response.json()
print(result)

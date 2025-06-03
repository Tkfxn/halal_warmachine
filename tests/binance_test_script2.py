import requests
import hmac
import hashlib
import time
import urllib.parse

# Replace these with your actual API key and secret from Binance
api_key = "CueL87oLc7bJXTrzOIhu9EagkWY7ThhXlX6UkzQ96JYcExEYmOhd7dooHw6HeHwC"
secret_key = "DG8S1PRbdLPHTkuevY92qsB4DzPHZIaFOzYQiEZp3l0HCIOt2RM6ZmdTPkHUdPMM"

base_url = "https://api.binance.com"
endpoint = "/api/v3/account"
timestamp = str(int(time.time() * 1000))

params = {
    "timestamp": timestamp
}
query_string = urllib.parse.urlencode(params)
signature = hmac.new(
    secret_key.encode('utf-8'),
    query_string.encode('utf-8'),
    hashlib.sha256
).hexdigest()

final_url = f"{base_url}{endpoint}?{query_string}&signature={signature}"
print("Request URL:", final_url)

headers = {
    "X-MBX-APIKEY": api_key
}

response = requests.get(final_url, headers=headers)
print("Response JSON:", response.json())

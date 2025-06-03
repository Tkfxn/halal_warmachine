# ✅ File: binance_debug_test.py (save to halal_warmachine/)
from binance.client import Client
from binance.exceptions import BinanceAPIException
import yaml

def get_keys():
    with open("config/settings.yml", "r") as f:
        cfg = yaml.safe_load(f)
    return cfg["binance"]["api_key"], cfg["binance"]["api_secret"]

def test_signature():
    api_key, api_secret = get_keys()
    print(f"Testing with API KEY: {api_key[:8]}... and SECRET: {api_secret[:8]}...")

    try:
        client = Client(api_key, api_secret)
        info = client.get_account()
        print("✅ API Signature is VALID.")
        print(f"Account info (truncated): {str(info)[:200]}")
    except BinanceAPIException as e:
        print(f"❌ Binance API Error: {e}")
    except Exception as e:
        print(f"❌ General Error: {e}")

if __name__ == "__main__":
    test_signature()

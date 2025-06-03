# === wallet_watcher.py ===
# Monitors profitable wallets using block explorers

import requests
import time
from utils.logging import log_wallet_activity
from utils.strategy import evaluate_wallet_behavior

WALLETS_TO_TRACK = [
    # Add wallet addresses here
    "0x123abc...",
    "0x456def...",
]

SCAN_APIS = {
    "ETH": "https://api.etherscan.io/api",
    "BSC": "https://api.bscscan.com/api",
    # Add Solana if needed with a wrapper or integration
}

API_KEYS = {
    "ETH": "YourEtherscanAPIKey",
    "BSC": "YourBscScanAPIKey",
}


def fetch_transactions(wallet, chain):
    try:
        url = SCAN_APIS[chain]
        params = {
            "module": "account",
            "action": "txlist",
            "address": wallet,
            "startblock": 0,
            "endblock": 99999999,
            "sort": "desc",
            "apikey": API_KEYS[chain],
        }
        res = requests.get(url, params=params)
        data = res.json()
        if data["status"] == "1":
            return data["result"][:5]  # limit to last 5
        return []
    except Exception as e:
        print(f"Error fetching {wallet} on {chain}: {e}")
        return []


def track_wallets():
    while True:
        for chain in SCAN_APIS:
            for wallet in WALLETS_TO_TRACK:
                txs = fetch_transactions(wallet, chain)
                for tx in txs:
                    if evaluate_wallet_behavior(tx):
                        log_wallet_activity(wallet, tx)
        time.sleep(180)  # every 3 minutes


if __name__ == "__main__":
    track_wallets()

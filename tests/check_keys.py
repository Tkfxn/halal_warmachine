import yaml

with open("config/settings.yml", "r") as f:
    cfg = yaml.safe_load(f)
    print("✅ API KEY FROM FILE:", cfg["binance"]["api_key"])
    print("✅ API SECRET FROM FILE:", cfg["binance"]["api_secret"])

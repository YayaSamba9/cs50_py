import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
else:
    try:
        btcoin = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey")
        btcoin.raise_for_status()
        data = btcoin.json()
        bt_price =float(data["data"]["priceUsd"])
        value = float(sys.argv[1])
    except requests.RequestException as e:
        sys.exit(f"Error fetching data: {e}")
    except (KeyError, ValueError):
        sys.exit("Error parsing data")

    amount = bt_price * value
    print(f"${amount:,.4f}")

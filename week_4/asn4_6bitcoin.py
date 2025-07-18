import json
import requests
import sys

if len(sys.argv)==1:
    sys.exit("Missing command-line argument")
try:
    n=float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")
got=requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=8c3b07839a83bf7dd67180942e423097a598b67a953b8e48eb413b7e3b9ba477")
x=got.json()["data"]
price=float(x["priceUsd"])
y=float(f"{price*n:.04f}")
print(f"${y:,}")

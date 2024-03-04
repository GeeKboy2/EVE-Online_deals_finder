import requests

endpoint = f"https://scripts.luawl.com/17293/sasware_AO.lua"
response = requests.get(endpoint)
if response.status_code == 200:
    data = response.json()
else:
    print(f"Error {response.status_code}: {response.reason}")

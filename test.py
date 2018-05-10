import requests
import json

url = 'http://127.0.0.1:32776/score'
headers = {'Content-Type':'application/json'}

print ("\nPredict - https://raw.githubusercontent.com/BaoxiJia/Shares/master/10000003.jpg")

data = "{\"url\":\"https://raw.githubusercontent.com/BaoxiJia/Shares/master/10000003.jpg\"}"
body = str.encode(json.dumps(data))
resp = requests.post(url, data, headers=headers)
print(resp.text)
results = json.loads(resp.text)
print("Rebar number is " + str(results['predictions']))

print ("\nPredict - https://raw.githubusercontent.com/BaoxiJia/Shares/master/10000035.jpg")

data = "{\"url\":\"https://raw.githubusercontent.com/BaoxiJia/Shares/master/10000035.jpg\"}"
body = str.encode(json.dumps(data))
resp = requests.post(url, data, headers=headers)
print(resp.text)
results = json.loads(resp.text)
print("Rebar number is " + str(results['predictions']))

print ("\nPredict - https://raw.githubusercontent.com/BaoxiJia/Shares/master/10000092.jpg")

data = "{\"url\":\"https://raw.githubusercontent.com/BaoxiJia/Shares/master/10000092.jpg\"}"
body = str.encode(json.dumps(data))
resp = requests.post(url, data, headers=headers)
print(resp.text)
results = json.loads(resp.text)
print("Rebar number is " + str(results['predictions']))

import json

data = []
with open("trump_tweets.json") as jsonFile:
	data = json.loads(jsonFile.read())



for i in data:
	print(i["text"])
	print(i["user"]["screen_name"])
	print("----")
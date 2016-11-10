import json

f = open('data.json')
data = json.load(f)

target = ''
matchframe = []
matches = []

for item in data:
	if item['selfName'] == target:
		matchframe = item['matchIDs']
		break

for serie in matchframe:
	matches.extend(serie)
	
f_match = open('file','w')
for i in matches:
	f_match.write(i + '\n')

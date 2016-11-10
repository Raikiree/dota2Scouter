import json

dire = json.load(open('dire.json'))
radiant = json.load(open('radiant.json'))


f = open('radiant.txt','w')
for item in radiant:
	team = item['selfName']
	matches = item['matchIDs']
	times = item['time']

	f.write(team + '\n')
	for i in range(20):
		time = times[i].split('-')
		if int(time[1]) > 10 or (int(time[1]) == 10 and int(time[2]) > 25):
			match = matches[i]
			f.write(match + '\n')
	f.write('\n')
f.close()


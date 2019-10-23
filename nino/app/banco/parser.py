import json

with open("datatemplate.json","r") as data:
	x = json.load(data)
'''
for i in x['Suite'] :
	print(i)
	['JOHN FREDDY NIÑO DIAZ']
'''
print(x['Suites'][0]['Nomes'][1])
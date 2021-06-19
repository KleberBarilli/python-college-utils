import json

with open('file.json') as json_file:
    data = json.load(json_file)
   
    lista =  []
    for p in data['utterances']:
    	lista.append(p)

for i in lista:
	intent = (i['intent'])
	if 'LocalGov.Waste' in intent or 'LocalGov.Bin' in intent :
		#print(intent)
		parsed = i
		print(json.dumps(parsed, indent = 4, sort_keys = True))
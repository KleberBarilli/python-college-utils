import csv, json
csvFilePath = "file.csv"

 #reading csv and adding data to dictionary
data = {}
with open(csvFilePath) as csvFile:
	csvReader = csv.DictReader(csvFile)
		
	for csvRow in csvReader:
		date = csvRow['Date']
		data[date] = csvRow #write to json file
with open('jsonFilePath.json', 'w') as jsonFile:
	jsonFile.write(json.dumps(data, indent=4))
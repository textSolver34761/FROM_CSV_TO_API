def from_csv_to_API(self, pathToFile, NameOfTheOutputSendToTheBrowser, nameOfTheGETRoute):
    import requests
    import csv
    import json
    from flask import Flask, json

    jsonArray = []
    #read csv file
    with open(r'pathToFile') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)
        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            jsonArray.append(row)
    #convert python jsonArray to JSON String and write to file
    with open(r'NameOfTheOutputSendToTheBrowser'+'.json', 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)

    api = Flask(__name__)

    @api.route('/'+'nameOfRoute', methods=['GET'])
    def twitts():
        return json.dumps(jsonString)

    if __name__ == '__main__':
        api.run()



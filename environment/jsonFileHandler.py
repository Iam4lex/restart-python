import json

def readJsonFile(fileName):
    
    data=""
    
    def readJsonFile(fileName):
    data = ""
    with open('files/insulin.json') as json_file:
        data = json.load(json_file)
    return data
    
    def readJsonFile(fileName):
    data = ""
    try:
        with open(fileName) as json_file:
            data = json.load(json_file)
    except IOError:
        print("Could not read file")
    return data
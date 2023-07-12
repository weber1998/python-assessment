from JsonModel import JsonModel
import json
def readJsonFile():
    jsonFilePath = '../Task1_PPTX_report/sample.json'
    with open(jsonFilePath) as f:
        data = json.load(f)
    return data
def main():

    jsonModel = JsonModel()
    data = readJsonFile()
    jsonModel.set_data(data)
    ujData = jsonModel.get_data()
    print(ujData)

if __name__ == '__main__':
    main()



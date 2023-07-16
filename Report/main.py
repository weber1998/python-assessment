from JsonModel import JsonModel
from ToPptx import ToPptx
from create_dat import Create_dat
import json

def read_json_file():
    json_file_path = '../Task1_PPTX_report/sample.json'
    with open(json_file_path) as f:
        data = json.load(f)
    return data
def main():

    create_dat = Create_dat()
    create_dat.write()

    json_model = JsonModel()
    data = read_json_file()
    json_model.set_data(data)

    new_data = json_model.get_data()

    to_pptx = ToPptx(new_data)
    to_pptx.presentation_build()
    to_pptx.save('example_output.pptx')

if __name__ == '__main__':
    main()



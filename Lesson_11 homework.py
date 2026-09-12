import yaml
import json
import pandas as pd



class Information:
    data: list

    def __init__(self):
        self.data = [
            {
                "Name": "Ilya",
                "Age": "28",
                "Job": "ATC",
                "Experience(years)": "5"
            },
            {
                "Name": "Alexander",
                "Age": "34",
                "Job": "Machine master",
                "Experience(years)": "3"
            },
            {
                "Name": "Daniil",
                "Age": "28",
                "Job": "IT",
                "Experience(years)": "6"
            }
        ]

    def add_data(self, data: list):
        self.data = self.data + data

    def yaml_loading(self):
        with open(r'data.yaml', 'w') as file:
            files = yaml.dump(self.data, file)

    def yaml_opening(self):
        with open(r'data.yaml') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            print(data)
            print(type(data))

    def json_loading(self):
        json_object = json.dumps(self.data, indent=1)
        with open("data.json", "w") as outfile:
            outfile.write(json_object)

    def json_opening(self):
        with open("data.json") as openfile:
            json_object = json.load(openfile)
            print(json_object)
            print(type(json_object))

    def csv_loading(self):
        df1 = pd.DataFrame(self.data)
        df1.to_csv("data.csv", index=False)

    def csv_opening(self):
        df1 = pd.DataFrame(self.data)
        print(df1)
        print(type(df1))


o_data = Information()
o_data.yaml_loading()
o_data.yaml_opening()
o_data.json_loading()
o_data.json_opening()
o_data.csv_loading()
o_data.csv_opening()
print('____________________________________________________________')
o_data.add_data([{
    "Name": "Ivan",
    "Age": "18",
    "Job": "Doctor",
    "Experience(years)": "0"
}])
o_data.yaml_loading()
o_data.json_loading()
o_data.csv_loading()


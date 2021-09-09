# imports
import csv
import json
import pandas as pd
import yaml

# function to convert csv to json
def csv_to_json(csv_file):
    with open(csv_file, 'r',encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        json_file = json.dumps([row for row in csv_reader])
        return json_file


# export json to desktop
json_export=csv_to_json("/Users/srikarprayaga/Desktop/DataEngineering-Assessment/orders.csv")
with open("/Users/srikarprayaga/Desktop/test.json", "w") as json_file:
    json.dump(json_export, json_file)

# just test if csv to json works locally 
json_export=csv_to_json("/Users/srikarprayaga/Desktop/DataEngineering-Assessment/orders.csv")
json_ex=csv_to_json("/Users/srikarprayaga/Desktop/DataEngineering-Assessment/test.csv")


###############################################################################
# convert json to csv
def json_to_csv(json_file):
    xda=pd.read_json(json_file)
    return xda.to_csv('/Users/srikarprayaga/Desktop/tester.csv',index=False)
json_to_csv(json_ex)

###############################################################################

# convert from yaml to json 
def yaml_json(yaml_file):
    with open(yaml_file, 'r') as yaml_file:
        yaml_data=yaml.load(yaml_file)
        json_data=json.dumps(yaml_data)
        return json_data
# convert yaml to csv
def yaml_to_csv(yaml_file):
    with open(yaml_file, 'r') as yaml_file:
        yaml_data=yaml.load(yaml_file)
        csv_data=pd.DataFrame(yaml_data)
        return csv_data.to_csv('/Users/srikarprayaga/Desktop/yaml_tester.csv',index=False)
# convert json to yaml
def json_to_yaml(json_file):
    with open(json_file, 'r') as json_file:
        json_data=json.load(json_file)
        yaml_data=yaml.dump(json_data)
        return yaml_data
# convert csv to yaml
def csv_to_yaml(csv_file):
    with open(csv_file, 'r') as csv_file:
        csv_data=pd.read_csv(csv_file)
        yaml_data=yaml.dump(csv_data)
        return yaml_data





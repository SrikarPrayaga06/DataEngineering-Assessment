import csv
import json
class convert:
    # one frunction to convert betwen csv, json , and yaml files
    def convert_csv_json(self, file_name, file_type):
        # open the file
        with open(file_name, 'r') as file:
            # read the file
            read_file = csv.DictReader(file)
            # create a list
            json_list = []
            # loop through the file
            for line in read_file:
                # add each line to the list
                json_list.append(line)
            # convert the list to json
            json_data = json.dumps(json_list)
            # write the json data to a file
            with open(file_name + '.json', 'w') as json_file:
                json_file.write(json_data)
            # return the json data
            return json_data
    def convert_json_csv(self, file_name, file_type):
        # open the file
        with open(file_name, 'r') as file:
            # read the file
            read_file = json.load(file)
            # create a list
            csv_list = []
            # loop through the file
            for line in read_file:
                # add each line to the list
                csv_list.append(line)
            # convert the list to csv
            csv_data = csv.DictWriter(csv_list)
            # write the csv data to a file
            with open(file_name + '.csv', 'w') as csv_file:
                csv_file.write(csv_data)
            # return the csv data
            return csv_data
    def convert_json_yaml(self, file_name, file_type):
        # open the file
        with open(file_name, 'r') as file:
            # read the file
            read_file = json.load(file)
            # create a list
            yaml_list = []
            # loop through the file
            for line in read_file:
                # add each line to the list
                yaml_list.append(line)
            # convert the list to yaml
            yaml_data = yaml.dump(yaml_list)
            # write the yaml data to a file
            with open(file_name + '.yaml', 'w') as yaml_file:
                yaml_file.write(yaml_data)
            # return the yaml data
            return yaml_data
    def convert_yaml_json(self, file_name, file_type):
        # open the file
        with open(file_name, 'r') as file:
            # read the file
            read_file = yaml.load(file)
            # create a list
            json_list = []
            # loop through the file
            for line in read_file:
                # add each line to the list
                json_list.append(line)
            # convert the list to json
            json_data = json.dumps(json_list)
            # write the json data to a file
            with open(file_name + '.json', 'w') as json_file:
                json_file.write(json_data)
            # return the json data
            return json_data
    def convert_yaml_csv(self, file_name, file_type):
        # open the file
        with open(file_name, 'r') as file:
            # read the file
            read_file = yaml.load(file)
            # create a list
            csv_list = []
            # loop through the file
            for line in read_file:
                # add each line to the list
                csv_list.append(line)
            # convert the list to csv
            csv_data = csv.DictWriter(csv_list)
            # write the csv data to a file
            with open(file_name + '.csv', 'w') as csv_file:
                csv_file.write(csv_data)
            # return the csv data
            return csv_data
    def convert_csv_yaml(self, file_name, file_type):
        # open the file
        with open(file_name, 'r') as file:
            # read the file
            read_file = csv.DictReader(file)
            # create a list
            yaml_list = []
            # loop through the file
            for line in read_file:
                # add each line to the list
                yaml_list.append(line)
            # convert the list to yaml
            yaml_data = yaml.dump(yaml_list)
            # write the yaml data to a file
            with open(file_name + '.yaml', 'w') as yaml_file:
                yaml_file.write(yaml_data)
            # return the yaml data
            return yaml_data
    def convert_yaml_yaml(self, file_name, file_type):
        # open the file
        with open(file_name, 'r') as file:
            # read the file
            read_file = yaml.load(file)
            # create a list
            yaml_list = []
            # loop through the file
            for line in read_file:
                # add each line to the list
                yaml_list.append(line)
            # convert the list to yaml
            yaml_data = yaml.dump(yaml_list)
            # write the yaml data to a file
            with open(file_name + '.yaml', 'w') as yaml_file:
                yaml_file.write(yaml_data)
            # return the yaml data
            return yaml_data
    def convert_json_yaml(self, file_name, file_type):
        # open the file
        with open(file_name, 'r') as file:
            # read the file
            read_file = json.load(file)
            # create a list
            yaml_list = []
            # loop through the file
            for line in read_file:
                # add each line to the list
                yaml_list.append(line)
            # convert the list to yaml
            yaml_data = yaml.dump(yaml_list)
            # write the yaml data to a file
            with open(file_name + '.yaml', 'w') as yaml_file:
                yaml_file.write(yaml_data)
            # return the yaml data
            return yaml_data
    def convert_yaml_json(self, file_name, file_type):
        # open the file
        with open(file_name, 'r') as file:
            # read the file
            read_file = yaml.load(file)
            # create a list
            json_list = []
            # loop through the file
            for line in read_file:
                # add each line to the list
                json_list.append(line)
            # convert the list to json
            json_data = json.dumps(json_list)
            # write the json data to a file
            with open(file_name + '.json', 'w') as json_file:
                json_file.write(json_data)
            # return the json data
            return json_data
    def convert_yaml_csv(self, file_name, file_type):
        # open the file
        with open(file_name, 'r') as file:
            # read the file
            read_file = yaml.load(file)
            # create a list
            csv_list = []
            # loop through the file
            for line in read_file:
                # add each line to the list
                csv_list.append(line)
            # convert the list to csv
            csv_data = csv.DictWriter(csv_list)
            # write the csv data to a file
            with open(file_name + '.csv', 'w') as csv_file:
                csv_file.write(csv_data)
            # return the csv data
            return csv_data
    def convert_csv_yaml(self, file_name, file_type):
        # open the file
        with open(file_name, 'r') as file:
            # read the file
            read_file = csv.DictReader(file)
            # create a list
            yaml_list = []
            # loop through the file
            for line in read_file:
                # add each line to the list
                yaml_list.append(line)
            # convert the list to yaml
            yaml_data = yaml.dump(yaml_list)
            # write the yaml data to a file
            with open(file_name + '.yaml', 'w') as yaml_file:
                yaml_file.write(yaml_data)
            # return the yaml data
            return yaml_data

    
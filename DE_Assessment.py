#4.	Write python code that can take csv and convert it into an array of json OR take an array of JSON and convert it into a CSV file with the same column names. This code should be able to write to a file in either CSV or JSON format, the user should be able to pick the output type. If someone picks the same output type as the input type it should write out that file still.
# csv contains columns id, name, description, commas_used, created_at, updated_at
import csv
import json
csv_file = '/Users/srikarprayaga/Desktop/orders.csv'
def csv_to_json(csv_file):
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        columns = next(reader)
        json_data = []
        for row in reader:
            json_data.append(dict(zip(columns, row)))
    return json_data
def json_to_csv(json_file):
    with open(json_file, 'r') as f:
        reader = csv.reader(f)
        columns = next(reader)
        csv_data = []
        for row in reader:
            csv_data.append(dict(zip(columns, row)))
    return csv_data
# export csv to json 
json_data = csv_to_json(csv_file)
json_file = '/Users/srikarprayaga/Desktop/orders.json'
with open(json_file, 'w') as f:
    json.dump(json_data, f)
# export json to csv
columns = ['id', 'name', 'description', 'commas_used', 'created_at', 'updated_at']
csv_file = '/Users/srikarprayaga/Desktop/orders.csv'
csv_data = json_to_csv(json_file)
with open(csv_file, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(columns)
    for row in csv_data:
        writer.writerow(row.values())



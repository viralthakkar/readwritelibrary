import csv
import json


class FileConverter:
    def __init__(self, input_filename, output_filename):
        self.input_filename = input_filename
        self.output_filename = output_filename

    def csv_to_json(self):
        with open(self.input_filename, mode='r') as file:
            reader = csv.DictReader(file)
            data = list(reader)

        with open(self.output_filename, mode='w') as file:
            json.dump(data, file, indent=4)

    def json_to_csv(self):
        with open(self.input_filename, mode='r') as file:
            data = json.load(file)

        with open(self.output_filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)


# Example usage:
converter = FileConverter('data.csv', 'converter-data.json')
converter.csv_to_json()

converter = FileConverter('data.json', 'converter_data_output.csv')
converter.json_to_csv()

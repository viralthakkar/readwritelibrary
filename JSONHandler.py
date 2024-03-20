import json
import os

class JSONHandler:
    def __init__(self, filename, batch_size=3, output_dir="output"):
        self.filename = filename
        self.batch_size = batch_size
        self.output_dir = output_dir

        os.makedirs(self.output_dir, exist_ok=True)

    def write_to_json_in_memory(self, data):
        with open(self.filename, mode='w') as file:
            json.dump(data, file, indent=4)
        print("Data has been written to", self.filename)

    def write_to_json_in_chunks(self, data):
        for i, chunk in enumerate(self._chunk_data(data), start=1):
            chunk_filename = os.path.join(self.output_dir, f"chunk_{i}.json")
            with open(chunk_filename, mode='w') as file:
                json.dump(chunk, file, indent=4)
            print(f"Chunk {i} has been written to {chunk_filename}")

    def read_from_json_in_memory(self):
        with open(self.filename, mode='r') as file:
            data = json.load(file)
        return data

    def read_from_json_in_chunks(self):
        with open(self.filename, mode='r') as file:
            data = json.load(file)
            for chunk in self._chunk_data(data):
                yield chunk

    def _chunk_data(self, data):
        for i in range(0, len(data), self.batch_size):
            yield data[i:i+self.batch_size]


if __name__ == '__main__':
    # Example usage:
    json_handler = JSONHandler('data.json', batch_size=3)

    # Writing data to JSON in memory
    data_to_write = [
        {"Name": "John", "Age": 25, "Location": "New York"},
        {"Name": "Alice", "Age": 30, "Location": "San Francisco"},
        {"Name": "Bob", "Age": 35, "Location": "Chicago"},
        {"Name": "John", "Age": 25, "Location": "New York"},
        {"Name": "Alice", "Age": 30, "Location": "San Francisco"},
        {"Name": "Bob", "Age": 35, "Location": "Chicago"},
        {"Name": "John", "Age": 25, "Location": "New York"},
        {"Name": "Alice", "Age": 30, "Location": "San Francisco"},
        {"Name": "Bob", "Age": 35, "Location": "Chicago"}
    ]
    json_handler.write_to_json_in_memory(data_to_write)

    # Writing data to JSON in chunks
    json_handler.write_to_json_in_chunks(data_to_write)

    # Reading data from JSON in memory
    data_read_memory = json_handler.read_from_json_in_memory()
    print("Data read from JSON in memory:", data_read_memory)

    # Reading data from JSON in chunks
    for chunk in json_handler.read_from_json_in_chunks():
        print("Data read from JSON in chunks:", chunk)

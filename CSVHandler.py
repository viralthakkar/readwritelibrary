import csv
import os


class CSVHandler:
    def __init__(self, filename, batch_size=3, output_dir="output"):
        self.filename = filename
        self.batch_size = batch_size

        self.output_dir = output_dir

        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)

    def write_to_csv(self, data):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print("Data has been written to", self.filename)

    def write_to_csv_in_chunks(self, data):
        header = data[0]
        for i, chunk in enumerate(self._chunk_data(data[1:]), start=1):
            chunk_filename = os.path.join(self.output_dir, f"chunk_{i}.csv")
            with open(chunk_filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(header)
                writer.writerows(chunk)
            print(f"Chunk {i} has been written to {chunk_filename}")

    def _chunk_data(self, data):
        for i in range(0, len(data), self.batch_size):
            yield data[i:i+self.batch_size]

    def read_from_csv(self):
        with open(self.filename, mode='r') as file:
            reader = csv.reader(file)
            header = next(reader)
            print("CSV Header:", header)
            data = [row for row in reader]
        return data

    def read_large_csv(self):
        with open(self.filename, mode='r') as file:
            reader = csv.reader(file)
            header = next(reader)
            print("CSV Header:", header)
            for row in reader:
                yield row

    def read_csv_in_batches(self):
        with open(self.filename, mode='r') as file:
            reader = csv.reader(file)
            header = next(reader)
            print("CSV Header:", header)
            batch = []
            for row in reader:
                batch.append(row)
                if len(batch) == self.batch_size:
                    yield batch
                    batch = []
            if batch:
                yield batch


if __name__ == '__main__':
    # Example usage:
    csv_handler = CSVHandler('data.csv')

    # Writing data to CSV
    data_to_write = [
        ['Name', 'Age', 'Location'],
        ['John', 25, 'New York'],
        ['Alice', 30, 'San Francisco'],
        ['Bob', 35, 'Chicago'],
        ['Name', 'Age', 'Location'],
        ['John', 25, 'New York'],
        ['Alice', 30, 'San Francisco'],
        ['Bob', 35, 'Chicago'],
        ['Name', 'Age', 'Location'],
        ['John', 25, 'New York'],
        ['Alice', 30, 'San Francisco'],
        ['Bob', 35, 'Chicago'],
        ['Name', 'Age', 'Location'],
        ['John', 25, 'New York'],
        ['Alice', 30, 'San Francisco'],
        ['Bob', 35, 'Chicago']
    ]
    csv_handler.write_to_csv_in_chunks(data_to_write)
    #
    # # Reading data from CSV
    # data_read = csv_handler.read_from_csv()
    # for row in data_read:
    #     print(row)
    #
    # for row in csv_handler.read_large_csv():
    #     print(row)


    for batch in csv_handler.read_csv_in_batches():
        # Process each batch of rows here
        print(batch)
import os


class TextHandler:
    def __init__(self, filename, output_dir="output"):
        self.filename = filename
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def write_to_txt(self, data):
        with open(self.filename, mode='w') as file:
            file.write(data)
        print("Data has been written to", self.filename)

    def read_from_txt(self):
        with open(self.filename, mode='r') as file:
            data = file.read()
        return data


if __name__ == '__main__':
    text_handler = TextHandler('data.txt')

    # Writing data to TXT
    data_to_write = "This is some text data."
    text_handler.write_to_txt(data_to_write)

    # Reading data from TXT
    data_read = text_handler.read_from_txt()
    print(data_read)

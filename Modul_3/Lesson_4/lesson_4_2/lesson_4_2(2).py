from abc import ABC, abstractmethod


class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass


class TextFileHandler(FileHandler):
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        with open(self.file_name, 'r') as file:
            content = file.read()
            print(f"Read text file: {content}")

    def write(self, data):
        with open(self.file_name, 'w') as file:
            file.write(data)
            print("Text data was written to a file")


class BinaryFileHandler(FileHandler):
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        with open(self.file_name, 'rb') as file:
            content = file.read()
            print(f"Read binary file: {content}")

    def write(self, data):
        with open(self.file_name, 'wb') as file:
            file.write(data.encode('utf-8'))
            print("Binary data was written to a file")


def save_data(handler: FileHandler, data):
    handler.write(data)
    handler.read()


# Пример использования:
text_handler = TextFileHandler("text_file.txt")
binary_handler = BinaryFileHandler("binary_file.bin")

save_data(text_handler, "This is text data")
save_data(binary_handler, "1101010101010")  # Хотя передается строка, она записывается в бинарный файл

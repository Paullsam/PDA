class FileReader:

    def __init__(self, file_adress):
        self.file_adress = file_adress

    def read(self):
        try:
            with open(self.file_adress, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return ""
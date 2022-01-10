import os.path
import tempfile


class File:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file
        if os.path.exists(path_to_file):
            return
        else:
            with open(path_to_file, 'w') as new_file:
                new_file.close()

    def read(self):
        result = ''
        if os.path.exists(self.path_to_file):
            with open(self.path_to_file, 'r') as text_file:
                result = text_file.read()
                text_file.close()
        else:
            return 'File does not exist'
        return result

    def write(self, text):
        self.text = text
        with open(self.path_to_file, 'w') as text_file:
            text_file.write(text)
            text_file.close()

    def __str__(self):
        return self.path_to_file

    def __iter__(self):
        with open(self.path_to_file, 'r') as text_file:
            result = text_file.readlines()
            return iter(result)

    def __add__(self, other):
        out_file = File(os.path.join(tempfile.gettempdir(), tempfile.NamedTemporaryFile().name))
        result = self.read() + other.read()
        out_file.write(result)
        return out_file

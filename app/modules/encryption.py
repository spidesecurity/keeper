from encryption.aes import AES
from utils.exceptions import *

import json


class EncryptionFile:
    def __init__(self, path: str, key: str):
        self.path = path
        self.key = key
        self.data = None

    def read(self):
        try:
            with open(self.path, "rb") as file:
                self.data = json.loads(AES(self.key).decode(file.read()))
                return self.data
        
        except ValueError:
            raise InvalidPasswordError
    
    def write(self, data: dict = None):
        if data is None:
            data = self.data
        
        else:
            self.data = data
        
        with open(self.path, "wb") as file:
            file.write(AES(self.key).encode(json.dumps(data)))

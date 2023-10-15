from Crypto.Cipher import AES as aeslib

import hashlib


class AES:
    def __init__(self, key: str):
        self.key = hashlib.md5(key.encode("utf-8")).hexdigest().encode("utf-8")

    def encode(self, data):
        """ Encryption data """
        aes = aeslib.new(self.key, aeslib.MODE_EAX)
        cipher_text, tag = aes.encrypt_and_digest(data.encode())

        return b"SpideK" + cipher_text + tag + aes.nonce

    def decode(self, data):
        """ Decryption data """
        cipher = aeslib.new(self.key, aeslib.MODE_EAX, data[-16:])
        data = cipher.decrypt_and_verify(data[6:-32], data[-32:-16])

        return data.decode()

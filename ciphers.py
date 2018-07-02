import string
import random

class Cipher:

    def __init__(self):
        self.alphabet = list(string.printable)
        self.alphabet_rev = self.alphabet[::-1]
    
    def encrypt(self):
        raise NotImplementedError()

    def decrypt(self):
        raise NotImplementedError()

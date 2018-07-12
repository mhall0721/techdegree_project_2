import string
import random
import re


class Cipher:

    def __init__(self):
        self.alphabet = list(string.ascii_lowercase)
        self.alphabet_rev = self.alphabet[::-1]
    
    def encrypt(self):
        raise NotImplementedError()

    def decrypt(self):
        raise NotImplementedError()

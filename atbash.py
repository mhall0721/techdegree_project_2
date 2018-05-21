from ciphers import Cipher

class Atbash(Cipher):

    def __init__(self, *args, **kwargs):
        super().__init__()

        for key, value in kwargs.items():
            setattr(self, key, value)

    def encrypt(self, text):
        '''Atbash encryption:
        Matches letter to it's corresponding letter in a reversed alphabet.
        '''
        text = text.lower()

        alpha_position = [self.alphabet.index(letter) for letter in text]
        encrypted_value = ''.join([self.alphabet_rev[int(pos)] for pos in alpha_position])

        return encrypted_value.upper()

    def decrypt(self, text):
        '''Atbash decryption:
        To return original input, reference letter position in reversed alphabet.
        '''

        text = text.lower()

        alpha_position = [self.alphabet_rev.index(letter) for letter in text]
        decrypted_value = ''.join([self.alphabet[int(pos)] for pos in alpha_position])

        return decrypted_value.upper()
        

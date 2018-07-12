import os 

from ciphers import Cipher
from affine import Affine  
from atbash import Atbash
from keyword_cipher import Keyword


def clear():
    """Clears screen"""

    os.system('cls' if os.name == 'nt' else 'clear')


def user_interface():
    """Command line menu providing an option to either encrypt or decrypt a value.
    Add input settings required to perform the cipher process.
    """

    while True:
        clear()

        prompt = "Welcome to the Secret Messages project for the Treehouse Techdegree!\n\n"
        prompt += "Choose an option:\n"
        prompt += "1) (E)ncrypt\n"
        prompt += "2) (D)ecrypt\n\n"
        prompt += "Type (q) to quit.\n"

        user_input = str(input(prompt)).strip()

        encrypt_input = [1, '1', 'e']
        decrypt_input = [2, '2', 'd']
        valid_input = encrypt_input + decrypt_input + ['q']

        while user_input not in valid_input:
            user_input = input(prompt).strip()

        if user_input.lower() == "q":
            break

        if user_input in encrypt_input:
            encrypt_val = run_cipher()

            if encrypt_val == 'q':
                break

            print("\nYour encrypted message is: {}\n\n".format(encrypt_val))

        if user_input in decrypt_input:
            decrypt_val = run_cipher(encrypt=False)

            if decrypt_val == 'q':
                break

            print("\nYour decrypted message is: {}\n".format(decrypt_val))

        input("Press any key to continue.")


def run_cipher(encrypt=True):
    """Sub menu with a list of implemented ciphers."""
    global key_val     
    clear()
    prompt = "Choose a cipher to use:\n\n"
    prompt += "1) (Af)fine\n"
    prompt += "2) (At)bash\n"
    prompt += "3) (K)eyword\n\n"
    prompt += "Type (q) to quit.\n"


    user_input = input(prompt)

    affine_input = [1, '1', 'af']
    atbash_input = [2, '2', 'at']
    keyword_cipher_input = [3, '3', 'k']
    valid_input = affine_input + atbash_input + keyword_cipher_input

    if user_input.lower() == "q":
        return "q"

    while user_input not in valid_input:
        user_input = str(input(prompt))

    def ask_for_message():
        val_input = input("Enter message:\n")

        return val_input

    text = ask_for_message()

    while text.lower().isalpha() is False:
        print("Message must contain letters only.\n")
        text = ask_for_message()

    # Affine inputs
    if user_input in affine_input:
        aff_first_number = input("Please enter a beginning number for the Affine cipher (must be odd):\n")
        aff_second_number = input("Please enter an ending number for the Affine cipher:\n")

        while aff_first_number.isnumeric() is False \
                or int(aff_first_number) % 2 == 0 \
                or aff_second_number.isnumeric() is False:
            print("Value must contain numbers. First number must be odd.\n")
            aff_first_number = input("Please enter a beginning number for the Affine Cipher (must be odd):\n")
            aff_second_number = input("Please enter an ending number for the Affine cipher:\n")

        cipher = Affine(aff_first_number, aff_second_number)

    # Atbash inputs
    if user_input in atbash_input:
        cipher = Atbash()

    # Keyword inputs   
    if user_input in keyword_cipher_input:
        user_keyword = input("Please enter your keyword for the Keyword Cipher:\n")

        while text.lower().isalpha() is False:
            print("Message must contain letters only.\n")
            user_keyword = input("Please enter keyword for the Keyword Cipher:\n")

        cipher = Keyword(user_keyword)
    
    if encrypt:
        key_val = cipher.encrypt(text)

    else:
        key_val = cipher.decrypt(text)

    
    return key_val
            

if __name__ == "__main__":
    user_interface()

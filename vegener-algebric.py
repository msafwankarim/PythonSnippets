'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#       Author:     Safwan                                                                  #
#       Date:       Monday, ‎5 ‎April ‎2021, ‏‎5:36:01 PM                                        #
#                                                                                           #
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def encrypt(string: str, key: str) -> str:

    string = string.upper()
    key = key.upper()

    

    key_list = list(key)
    key_list = [chr(ord(key_list[i % len(key_list)])) for i in range(len(string))]
    

    encrypted_str = ""

    for i,letter in enumerate(string):
        if letter.isspace():
            encrypted_str += " "
        else:
            encrypted_str += chr(((ord(letter) + ord(key_list[i])) % 26) + ord('A'))

    return encrypted_str
    


def decrypt(string: str, key: str) -> str:
    string = string.upper()
    key = key.upper()
    key_list = list(key)
    decrypted_str = ""

    key_list = [chr(ord(key_list[i % len(key_list)])) for i in range(len(string))]
    
    for i,letter in enumerate(string):
        if letter.isspace():
            decrypted_str += " "
        else:
            decrypted_str += chr(((ord(letter) - ord(key_list[i])) % 26) + ord('A'))

    return decrypted_str

def main() -> None:
    source_str = input("Enter string to encrypt: ")
    key = input("Enter Key: ")

    encrypted = encrypt(source_str, key)
    print(f"Output: {encrypted}")
    print(f"Decryption: {decrypt(encrypted,key)}")
    pass


main()

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#       Author:     Safwan                                                                  #
#       Date:       Sunday, ‎4 ‎April ‎2021, ‏‎6:35:31 PM                                        #
#                                                                                           #
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

table = []


def populate_table():
    for i in range(26):
        alphabet_list = []
        for j in range(i, 26+i):
            alphabet_list.append(encode(j))
        table.append(alphabet_list)


def decode(char) -> int:
    return (ord(char) - 65) % 26


def encode(int_val) -> str:
    return chr((int_val % 26)+65)


def print_table():
    for i in table:
        print('|', ' '.join(i), '|')


def encrypt(string: str, key: str) -> str:

    string = string.upper()
    key = key.upper()

    key_list = list(key)
    key_list = [chr(ord(key_list[i % len(key_list)])) for i in range(len(string))]

    encrypted_str = ""

    for i, letter in enumerate(string):
        if letter.isspace():
            encrypted_str += " "
        else:
            encrypted_str += table[decode(key_list[i])][decode(letter)]

    return encrypted_str


def decrypt(string: str, key: str) -> str:
    string = string.upper()
    key = key.upper()

    key_list = list(key)
    key_list = [chr(ord(key_list[i % len(key_list)]))
                for i in range(len(string))]

    decrypted_str = ""
    for i in range(len(string)):
        if string[i].isspace():
            decrypted_str += " "
            continue
        for j, letter in enumerate(table[decode(key_list[i])]):
            if letter == string[i]:
                decrypted_str += table[0][j]

    return decrypted_str


def main():
    populate_table()
    print_table()

    source_str = input("Enter string to encrypt: ")
    key = input("Enter Key: ")

    encrypted = encrypt(source_str, key)
    print(f"Output: {encrypted}")
    print(f"Decryption: {decrypt(encrypted,key)}")
    pass


main()

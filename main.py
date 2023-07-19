from encode_pass import encode
from decode_pass import decode

if __name__ == "__main__":
    while True:
        print("Menu\n----------\n1. Encode\n2. Decode\n3. Quit\n")
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded_pass = encode(password)
            print("Your password has been encoded and stored!")
        elif option == 2:
            decoded_pass = decode(encoded_pass)
            print(f"The encoded password is {encoded_pass}, and the original password is {decoded_pass}.")
        elif option == 3:
            break


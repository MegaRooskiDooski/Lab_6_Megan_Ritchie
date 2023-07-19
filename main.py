from encode_pass import encode

if __name__ == "__main__":
    while True:
        print("Menu\n----------\n1. Encode\n2. Decode\n3. Quit\n")
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded_pass = encode(password)
            print("Your password has been encoded and stored!")
        elif option == 2:
            print(f"The encoded password is {encoded_pass}, and the original password is {password}.")
        elif option == 3:
            break


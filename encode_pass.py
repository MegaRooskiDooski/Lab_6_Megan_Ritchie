# Megan Ritchie

def encode(password):
    encoded_pass = ""
    for i in password:
        encoded_pass += str(int(i)+3)
    return  encoded_pass
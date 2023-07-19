def decode(password):
    decoded_pswd = ""
    for i in range(len(password)):
        decoded_pswd += str((int(password[i]) - 3))
    return decoded_pswd
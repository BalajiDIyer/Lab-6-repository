def encoder(password):
    encoded = ""
    for x in range (0, len(password)):
        if password[x] == '7': # if the new digit is over 10, then it is subtracted by 10
            encoded += '0'
        elif password[x] == '8':
            encoded += '1'
        elif password[x] == '9':
            encoded += '2'
        else:
            encoded += str(int(password[x]) + 3) # each digit is having 3 added to it

    return encoded

def decoder(encoded):
    decoded = ''
    for val in encoded:
        if val == '0':
            val = '7'
        elif val == '1':
            val = '8'
        elif val == '2':
            val = '9'
        else:
            val = int(val)-3
            val = str(val)
        decoded += val
    return decoded

def decode_pw(encoded):
    password = str()
    for i in str(encoded):
        if i == '3':
            password += '0'
        if i == '4':
            password += '1'
        if i == '5':
            password += '2'
        if i == '6':
            password += '3'
        if i == '7':
            password += '4'
        if i == '8':
            password += '5'
        if i == '9':
            password += '6'
        if i == '1':
            continue
        if i == '0':
            password += '7'
        if i == '2':
            password += '8'
        if i == '3':
            password += '9'
    return password
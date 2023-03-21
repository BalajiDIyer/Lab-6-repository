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

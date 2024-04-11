#Katarina Neal repository
def encoder(message):
    result = ''
    for digit in message:
        new_digit = str((int(digit) + 3) % 10)
        result += new_digit
    return result

def decoder(password):
    result = ''
    for digit in password:
        new_digit = str((int(digit) - 3) % 10)
        result += new_digit
    return result

#shirley - added the menu
def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    pass


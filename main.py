# Bailey Watkins
def encode(password):
    encoded_password = ""
    for char in password:
        newchar = str(int(char) + 3)
        encoded_password += str(int(newchar) % 10)
    return encoded_password
    
#Katarina Neal respitory(added decoder)


#shirley - added the menu
def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    pass

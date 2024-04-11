def decoder(password):
    result = ''
    for digit in password:
        new_digit = str((int(digit) - 3) % 10)
        result += new_digit
    return result

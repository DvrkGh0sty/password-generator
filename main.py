import random

def generate_passwd(length):
    chars = 'abcdefghijkklmnopqrstuvwxyz/01234567890#@!$*=+-'
    password = ''
    for char in range(length):
        char = random.choice(chars)
        password += char
    return password


def main():
    while True:
        length = int(input('How long would you like the passwd: '))
        if length >= 6:
            print(generate_passwd(length))
            break
        else:
            continue
main()


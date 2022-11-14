import time
import keyboard
import pyperclip

mode = input("a.Enycrption b.Dycrption: ")

def encrypt():
    passwd = input('Insert your password here: ')

    encrypted = passwd.replace('a', '!',).replace('b', '%').replace('c', '(').replace('d', '+').replace('e', '|').replace('f', '#').replace('g', '~').replace('h', '`').replace('i', '@').replace('j', '^').replace('k', ',').replace('l', '{').replace('m', '<').replace('n', '-').replace('o', '[').replace('p', '"').replace('q', ':').replace('r', ';').replace('s', '?').replace('t', '؟').replace('u', '$').replace('v', ',').replace('w', '.').replace('x', ']').replace('y', '}').replace('z', ')')

    time.sleep(0.5)
    print("Here is your encrypted password: " + encrypted)
    time.sleep(0.5)
    time.sleep(0.5)
    print("Password coppied to clipboard!")

    pyperclip.copy(encrypted)

    time.sleep(0.5)
    print("Press enter to exit")

    while True:
        if keyboard.is_pressed('enter'):
            break


def decrypt():
    passwd = input('Insert your password here: ')
    
    decrypted = passwd.replace('!', 'a',).replace('%', 'b').replace('(', 'c').replace('+', 'd').replace('|', 'e').replace('#', 'f').replace('~', 'g').replace('`', 'h').replace('@', 'i').replace('^', 'j').replace(',', 'k').replace('{', 'l').replace('<', 'm').replace('-', 'n').replace('[', 'o').replace('"', 'p').replace(':', 'q').replace(';', 'r').replace('?', 's').replace('؟', 't').replace('$', 'u').replace(',', 'v').replace('.', 'w').replace(']', 'x').replace('}', 'y').replace(')', 'z')

    time.sleep(0.5)
    print("Here is your decrypted password: " + decrypted)
    time.sleep(0.5)
    time.sleep(0.5)
    print("Password coppied to clipboard!")

    pyperclip.copy(decrypted)

    time.sleep(0.5)
    print("Press enter to exit")

    while True:
        if keyboard.is_pressed('enter'):
            break


if mode == "a":
    encrypt()

elif mode == "b":
    decrypt()
else:
    print(f"mode not recognized ({mode})")

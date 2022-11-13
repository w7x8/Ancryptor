import time
import keyboard
import pyperclip

mode = input("a.Enycrption b.Dycrption: ")
passwd = input('Insert your password here: ')
    
if mode == 'a':
    ancrypt = passwd.replace('a', '!',).replace('b', '%').replace('c', '(').replace('d', '+').replace('e', '|').replace('f', '#').replace('g', '~').replace('h', '`').replace('i', '@').replace('j', '^').replace('k', ',').replace('l', '{').replace('m', '<').replace('n', '-').replace('o', '[').replace('p', '"').replace('q', ':').replace('r', ';').replace('s', '?').replace('t', '؟').replace('u', '$').replace('v', ',').replace('w', '.').replace('x', ']').replace('y', '}').replace('z', ')')
elif mode == 'b':
    ancrypt = passwd.replace('!', 'a',).replace('%', 'b').replace('(', 'c').replace('+', 'd').replace('|', 'e').replace('#', 'f').replace('~', 'g').replace('`', 'h').replace('@', 'i').replace('^', 'j').replace(',', 'k').replace('{', 'l').replace('<', 'm').replace('-', 'n').replace('[', 'o').replace('"', 'p').replace(':', 'q').replace(';', 'r').replace('?', 's').replace('؟', 't').replace('$', 'u').replace(',', 'v').replace('.', 'w').replace(']', 'x').replace('}', 'y').replace(')', 'z')
else:
    print(f"mode not recognized ({mode})")

time.sleep(0.5)
print("Here is your encrypted password: " + ancrypt)
time.sleep(0.5)
print("Password coppied to clipboard!")

pyperclip.copy(ancrypt)

time.sleep(0.5)
print("Press enter to exit")

while True:
    if keyboard.is_pressed('enter'):
        break

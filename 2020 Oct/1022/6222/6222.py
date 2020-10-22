import sys
sys.stdin = open("6222.txt","r")

a = input()

if (65 <= ord(a) < 90):
    b = ord(a) + 32
    print('{}(ASCII: {}) => {}(ASCII: {})'.format(a, ord(a), chr(b), b))
elif (97 <= ord(a) < 122):
    b = ord(a) - 32
    print('{}(ASCII: {}) => {}(ASCII: {})'.format(a, ord(a), chr(b), b))
else:
    print('{}'.format(a))
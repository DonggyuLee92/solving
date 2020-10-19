import sys
sys.stdin = open("6220.txt","r")

a = input()

if (ord(a)>96):
    print("{} 는 소문자 입니다.".format(a))
else:
    print("{} 는 대문자 입니다.".format(a))
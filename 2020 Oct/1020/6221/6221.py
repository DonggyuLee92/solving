import sys
sys.stdin = open("6221.txt","r", encoding="UTF8")

a = input()
b = input()

if (a=="가위"):
    if (b=="가위"):
        print("Result : Draw")
    elif(b=="바위"):
        print("Result : Man2 Win!")
    else:
        print("Result : Man1 Win!")
elif (a=="바위"):
    if (b=="바위"):
        print("Result : Draw")
    elif(b=="보"):
        print("Result : Man2 Win!")
    else:
        print("Result : Man1 Win!")
else:
    if (b=="보"):
        print("Result : Draw")
    elif(b=="가위"):
        print("Result : Man2 Win!")
    else:
        print("Result : Man1 Win!")
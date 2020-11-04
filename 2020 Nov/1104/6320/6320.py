import sys
sys.stdin = open("6320.txt","r", encoding="UTF-8")

p1 = input()
p2 = input()
p1s = input()
p2s = input()

if (p1s=="가위"):
    if (p2s=="가위"):
        print("비겼습니다!")
    elif (p2s=="바위"):
        print("바위가 이겼습니다!")
    else:
        print("보가 이겼습니다!")
elif (p1s=="바위"):
    if(p2s=="바위"):
        print("비겼습니다!")
    elif(p2s=="보"):
        print("보가 이겼습니다!")
    else:
        print("가위가 이겼습니다!")
elif (p1s=="보"):
    if(p2s=="보"):
        print("비겼습니다!")
    elif(p2s=="가위"):
        print("가위가 이겼습니다!")
    else:
        print("보가 이겼습니다!")

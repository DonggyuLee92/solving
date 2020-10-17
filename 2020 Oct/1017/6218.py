import sys
# sys.stdin = ("6218.txt","r")

a = int(input())

for i in range(1, a+1):
    if(a%i==0):
        print("{}(은)는 {}의 약수입니다.".format(i,a))
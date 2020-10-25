import sys
sys.stdin= open("prime.txt","r")
# 소수인지 아닌지 확인하는 문제
# 소수라면 1 출력, 소수가 아니라면 약수 중 2번째로 작은 약수 출력

n = int(input())
check = 0
for i in range(1,n):
    if(n%i==0):
        check = check + 1
        if (check == 2):
            print(i)

if (check == 1):
    print(1)
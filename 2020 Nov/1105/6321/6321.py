a = int(input())
ans = 0
for i in range(1, a+1):
    if (a%i==0):
        ans = ans + 1

if (ans==2):
    print("소수입니다.")
else:
    print("소수가 아닙니다.")
import math

a = 9
ans = ''
while(a):
    answer = a%2
    a = math.floor(a/2)
    ans = str(answer) + ans
    if(a==0):
        break

print(ans)
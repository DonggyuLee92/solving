import sys


score = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
ans = 0
for i in score:
    if(i > 80):
        ans = ans + i

print(ans)
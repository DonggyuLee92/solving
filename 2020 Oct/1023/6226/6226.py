# import sys
# sys.stdin = open("6226.txt","r")

ans = ""
for i in range(1,200):
    if(i%7==0 and i%5!=0):
        ans = ans + str(i) + ","

print(ans[:-1])
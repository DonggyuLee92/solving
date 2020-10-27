ans = ""
for i in range(1,100):
    if (i%2==1):
        ans = ans + str(i) + ", "

print(ans[:-2])
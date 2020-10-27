ans = ""
for i in range(1, 101):
    if (i % 2 == 0):
        ans = ans + str(i) + " "

print(ans[:-1])
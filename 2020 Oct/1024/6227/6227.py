ans = ""
for i in range(200, 300):
    hund = int(i/100)
    tenn = int(i/10)
    if(hund%2==0 and tenn%2==0 and i%2==0):
        ans = ans + str(i) +","
print(ans[:-1])
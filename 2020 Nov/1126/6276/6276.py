
ans = []
answer = []
for i in range(2,10):
    for j in range(1,10):
        if(i*j %3 !=0 and i*j%7 != 0):
            ans.append(i*j)
    # print(ans)
    answer.append(ans)
    ans = []

print(answer)

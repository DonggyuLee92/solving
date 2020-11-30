ans = [1,1]
fibo = 1
for i in range(8):
    fibo = ans[-2] + ans[-1]
    ans.append(fibo)
print(ans)
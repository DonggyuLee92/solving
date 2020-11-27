[1, 2, 3, 4, 6, 12]


input_num = int(input())
ans = ''
for i in range(1, input_num+1):
    if input_num%i==0:
        ans = ans + str(i) + ', '


print("[{}]".format(ans[0:-2]))

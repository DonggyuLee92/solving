input_list = [12, 24, 35, 70, 88, 120, 155]
# ans = [x for i in input_list if x%2==0]
ans = []
check = 0
for i in input_list:
    check +=1
    if check%2==0:
        ans.append(i)


print(ans)

# print(input_list[0])
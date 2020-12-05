import sys
sys.stdin = open("6295.txt","r")

a, b = input().split(', ')
a = int(a)
b = int(b)
# print(a,b)
# print(type(b))

ans = [[0 for x in range(b)] for y in range(a)]

for i in range(a):
    # temp_ans = []
    for j in range(b):
        ans[i][j] = j*i
# ans_a.append(ans_b)

print(ans)
import sys
sys.stdin = open("6297.txt","r")

input_word = input().split(', ')
# print(input_word)
ans = ''
for i in input_word:
    if int(i)%2 == 1:
        ans = ans + i + ', '
print(ans[:-2])
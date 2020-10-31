# import sys, math
# sys.stdin = open("6249.txt", "r")
#
# a = int(input())
# # b = 110%10
# ans_0 = 0
# ans_1 = 0
# ans_2 = 0
# ans_3 = 0
# ans_4 = 0
# ans_5 = 0
# ans_6 = 0
# ans_7 = 0
# ans_8 = 0
# ans_9 = 0
# while(a):
#     if(a%10 == 0):
#         ans_0 = ans_0 + 1
#         a = math.floor(a/10)
#     elif(a%10 == 1):
#         ans_1 = ans_1 + 1
#         a = math.floor(a/10)
#     elif(a%10 == 2):
#         ans_2 = ans_2 + 1
#         a = math.floor(a/10)
#     elif (a % 10 == 3):
#         ans_3 = ans_3 + 1
#         a = math.floor(a/10)
#     elif (a % 10 == 4):
#         ans_4 = ans_4 + 1
#         a = math.floor(a/10)
#     elif (a % 10 == 5):
#         ans_5 = ans_5 + 1
#         a = math.floor(a/10)
#     elif (a % 10 == 6):
#         ans_6 = ans_6 + 1
#         a = math.floor(a/10)
#     elif (a % 10 == 7):
#         ans_7 = ans_7 + 1
#         a = math.floor(a/10)
#     elif (a % 10 == 8):
#         ans_8 = ans_8 + 1
#         a = math.floor(a/10)
#     else:
#         ans_9 = ans_9 + 1
#         a = math.floor(a/10)
#
#     if(a < 1):
#         break
#
# print("0 1 2 3 4 5 6 7 8 9")
# print("{} {} {} {} {} {} {} {} {} {}".format(ans_0, ans_1, ans_2, ans_3, ans_4, ans_5, ans_6, ans_7, ans_8, ans_9))
# # print(b)

# 여기까지 노가다

import sys
sys.stdin = open("6249.txt","r")

n = input()
num_list = [0] * 10
# num_list = [for 0 in range(10)]
ans = ""

for i in str(n):
    num_list[int(i)] = num_list[int(i)] + 1

for i in range(10):
    ans = ans + str(num_list[i]) + " "
print("0 1 2 3 4 5 6 7 8 9")
print(ans[:-1])
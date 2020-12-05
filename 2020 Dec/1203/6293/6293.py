import sys
import math
sys.stdin = open("6293.txt","r")

input_num = [int(x) for x in input().split(", ")]
# print(input_num)
# print(input_num[0])

ans = ""
for i in input_num:
    radi = 0
    radi = i * 2 * math.pi
    # print(round(radi,2))
    # print("%.2f" % radi)
    ans = ans + str(round(radi,2)) + ", "
print(ans[:-2])
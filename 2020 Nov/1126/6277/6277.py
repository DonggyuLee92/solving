import sys
sys.stdin = open("6277.txt","r")


input_list = [int(x) for i in range(5) for x in input().split('\n')]
# print(input_list)
avg = 0
for i in range(5):
    avg = avg + input_list[i]
print("입력된 값 {}의 평균은 {}입니다.".format(input_list, avg/5))
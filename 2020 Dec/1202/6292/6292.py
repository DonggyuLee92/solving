import sys
sys.stdin = open("6292.txt","r")


# # input_num = input().split(',')
# input_num = input()
# my_list = (input_num)
# my_tuple = [input_num]
# # for i in input_num:
# #     # print(i)
# #     my_list.append(i)
# # # print(input_num[1])
#
# print(input_num)
# print(list(input_num))


my_list = [int(n) for n in input().split(', ')]
my_tuple = tuple(my_list)

print(my_list)
print(my_tuple)
input_list = [1, 3, 11, 15, 23, 28, 37, 52, 85, 100]
# ans = []
# # print(input_list[1])
# for i in input_list:
#     if i % 2 == 0 :
#         ans.append(i)
#     # print(i)
# print(ans)
# ////////////////////////////////////////// 다른방법


ans = [x for x in input_list if x%2== 0]
print(ans)
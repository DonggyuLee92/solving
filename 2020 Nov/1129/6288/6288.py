# ans = []
#
# for i in range(1,21):
#     if i**2 % 15 != 0:
#         ans.append(i**2)
# print(ans)

ans = [x**2 for x in range(1,21) if x%3!=0 or x%5!=0]
print(ans)
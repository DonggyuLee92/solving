def long(str1, str2):
    if (len(str1)>len(str2)):
        print(str1)
    elif(len(str2)>len(str1)):
        print(str2)
    else:
        print("똑같다")

str1, str2 = map(str, input().split(', '))
long(str1, str2)
# print(len(str1))
# print(str2)

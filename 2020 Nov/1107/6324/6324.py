li = [1, 2, 3, 4, 3, 2, 1]

unique_list = list()

def unique_value(li):
    global unique_list
    for i in range(len(li)):
        num = li[i]
        if num not in unique_list:
            unique_list.append(num)

print(li)
unique_value(li)
print(unique_list)
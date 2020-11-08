li = [2, 4, 6, 8, 10]

def confirm(num, list):
    if (num in li):
        print("{} => True".format(num))
    else:
        print("{} => False".format(num))


print(li)
confirm(5, li)
confirm(10, li)

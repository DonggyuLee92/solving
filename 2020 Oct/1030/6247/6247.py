import sys

i = 7
j = 0
while(i):
    a = (" " * j)
    b = ("*" * i)
    print("{}{}".format(a,b))
    i = i-2
    j = j+1
    if j == 4:
        break
import sys

a = 5
for i in range(1,a+1):
    for j in range(a-i+1):
        blank = (" " * j)
        star = ("*" * i)

        ans = blank + star

    print(ans)
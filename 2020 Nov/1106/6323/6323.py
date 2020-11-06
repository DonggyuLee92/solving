num = int(input())

ans = "1, 1"
a = 1
b = 1

if(num==2):
    print("[{}]".format(ans))
for i in range(num-2):
    c = a + b
    a = b
    b = c
    ans = ans + ', ' + str(c)


print("[{}]".format(ans))
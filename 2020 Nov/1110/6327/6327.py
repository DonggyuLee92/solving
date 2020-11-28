# a = 2, 3

def square(a, b):
    ans_a = a * a
    ans_b = b * b
    print("square({}) => {}".format(a, ans_a))
    print("square({}) => {}".format(b, ans_b))

input = input()
a = int(input[0])
b = int(input[-1])
square(a, b)
# num = int(input())
ans = 0
def factorial(num):
    if (num>1):
        return num * factorial(num-1)
    else:
        return 1

print(factorial(5))


# def factorial(n):
#     if n == 1:  # n이 1일 때
#         return 1  # 1을 반환하고 재귀호출을 끝냄
#     return n * factorial(n - 1)  # n과 factorial 함수에 n - 1을 넣어서 반환된 값을 곱함
#
#
# print(factorial(5))
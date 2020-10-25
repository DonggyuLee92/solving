# answer = 0
#     for i in range(1, len(arr)):
#         if sum(arr[:i]) == sum(arr[i+1:]):
#             answer = i
#             break
#     return answer

# 4 1 2 3 3 입력
# 4는 배열의 크기
# [1,2,3,3]의 배열
# 앞에서부터 더해가다가 제일 마지막 배열의 수와 같아지면 그 수 출력
# 1+2 는 마지막 3이니 2 출력하는 문제
# 타임오버떠서 망함




answer = 0
    for i in range(1, len(arr)):
        if sum(arr[:i]) == arr[i+1]):
            answer = i
            break
    print(answer)
import sys
# 단어를 입력하면 마지막 글자와 뒤에서 두번째 글자 출력
# APPLE 입력하면 E L 출력

word = input()
ans = word[-1] + " " + word[-2]
print(ans)
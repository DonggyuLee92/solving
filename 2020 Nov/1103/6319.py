a = input()

print(a)
ans = ''
for i in str(a):
    ans = i + ans

if (a==ans):
    print(a)
    print("입력하신 단어는 회문(Palindrome)입니다.")
# input = {Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.}
import sys
sys.stdin = open("6275.txt","r")
input = input()
# input_list = list(input())
aeiou = ('aeiou')
ans = [i for i in input if i not in aeiou]

print(''.join(ans))
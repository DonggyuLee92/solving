import sys

blood = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
ans_a = 0
ans_b = 0
ans_o = 0
ans_ab = 0
for i in blood:
    if(i=='A'):
        ans_a = ans_a + 1
    elif(i=='B'):
        ans_b = ans_b + 1
    elif(i=='O'):
        ans_o = ans_o + 1
    else:
        ans_ab = ans_ab + 1



print("{'A': {}, 'O': {}, 'B': {}, 'AB': {}}".format(ans_a, ans_b, ans_o, ans_ab))
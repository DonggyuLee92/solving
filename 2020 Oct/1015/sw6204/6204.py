import sys
sys.stdin = open("6204.txt","r")

T = float(input())
cm = '%0.2f'  %(2.54 * T)
inch = '%0.2f' % T
print("{} inch =>  {} cm" .format(inch, cm))
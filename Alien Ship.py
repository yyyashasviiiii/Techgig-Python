import sys
import os

''' Read input from STDIN. Print your output to STDOUT '''
# Use input() to read input from STDIN and use print to write your output to STDOUT
# Write code here


h1, m1 = list(map(int, input().split()))
h2, m2 = list(map(int, input().split()))

ha, ma = 0, 0
print(h1)
print(m1)
ma = m1 + m2
ha = (h1 + h2 + (ma//60))%24
ma = ma % 60

print(f"{ha:02d}", f"{ma:02d}")

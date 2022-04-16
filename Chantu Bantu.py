import sys
import os

''' Read input from STDIN. Print your output to STDOUT '''
# Use input() to read input from STDIN and use print to write your output to STDOUT
# Write code here

t = int(input())
for j in range(t):
    n = int(input())
    g = int(input())
    sum = 0
    prices = list(map(int,input().split()))
    prices = sorted(prices)

    for i in range(n):
        sum = sum + prices[i]
    print(sum)



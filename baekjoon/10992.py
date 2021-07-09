#!/usr/bin/env python3
# Title : 별 찍기 - 17
# Link  : https://www.acmicpc.net/problem/10992

from sys import stdin

# 입력 빠르게 받기
input = stdin.readline

n = int(input())

for i in range(n):
    if i == 0:
        print(" " * (n - i - 1) + "*")
    elif i == n - 1:
        print("*" * ((2 * n) - 1))
    else:
        str = (" " * (n - i - 1)) + "*" + (" " * ((2 * i) - 1)) + "*"
        print(str)

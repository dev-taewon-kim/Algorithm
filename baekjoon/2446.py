#!/usr/bin/env python3
# Title : 별 찍기 - 9
# Link  : https://www.acmicpc.net/problem/2446

from sys import stdin

# 입력 빠르게 받기
input = stdin.readline

n = int(input())

for i in range(2 * n - 1):
    if i > n - 1:
        i = n - (i % n) - 2
    str = (" " * i) + ("*" * ((2 * n) - ((2 * i) + 1)))
    print(str)

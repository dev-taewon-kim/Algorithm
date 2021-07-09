#!/usr/bin/env python3
# Title : 별 찍기 - 16
# Link  : https://www.acmicpc.net/problem/10991

from sys import stdin

# 입력 빠르게 받기
input = stdin.readline

n = int(input())

for i in range(n):
    str = (" " * (n - i - 1)) + ("* " * (i + 1))
    str = str[:len(str) - 1]
    print(str)

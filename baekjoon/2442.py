#!/usr/bin/env python3
# Title : 별 찍기 - 5
# Link  : https://www.acmicpc.net/problem/2442

from sys import stdin

# 입력 빠르게 받기
input = stdin.readline

n = int(input())

for i in range(n):
    print((" " * (n - (i + 1))) + ("*" * ((2 * (i + 1)) - 1)))

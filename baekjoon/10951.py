#!/usr/bin/env python3
# Title : A+B - 4
# Link  : https://www.acmicpc.net/problem/10951

from sys import stdin

# 입력 빠르게 받기
input = stdin.readline

while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except ValueError:
        break

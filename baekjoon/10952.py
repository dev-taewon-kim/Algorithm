#!/usr/bin/env python3
# Title : A+B - 5
# Link  : https://www.acmicpc.net/problem/10952

from sys import stdin

# 입력 빠르게 받기
input = stdin.readline

while True:
    a, b = map(int, input().split())
    if (a and b):
        print(a + b)
    else:
        break
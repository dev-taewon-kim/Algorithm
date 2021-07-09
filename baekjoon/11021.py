#!/usr/bin/env python3
# Title : A+B - 7
# Link  : https://www.acmicpc.net/problem/11021

from sys import stdin

# 입력 빠르게 받기
input = stdin.readline

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    print(f"Case #{i + 1}: {a + b}")

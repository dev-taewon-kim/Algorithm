#!/usr/bin/env python3
# Title : 별 찍기 - 4
# Link  : https://www.acmicpc.net/problem/2441

from sys import stdin

# 입력 빠르게 받기
input = stdin.readline

n = int(input())

for i in range(n):
    print(" " * i + "*" * (n - i))

#!/usr/bin/env python3
# Title : 구구단
# Link  : https://www.acmicpc.net/problem/2739

from sys import stdin

# 입력 빠르게 받기
input = stdin.readline

n = int(input())

for i in range(9):
    print(f"{n} * {i + 1} = {n * (i + 1)}")

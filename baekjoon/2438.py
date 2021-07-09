#!/usr/bin/env python3
# Title : 별 찍기 - 1
# Link  : https://www.acmicpc.net/problem/2438

from sys import stdin

# 입력 빠르게 받기
input = stdin.readline

n = int(input())

for i in range(n):
    print("*" * (i + 1))

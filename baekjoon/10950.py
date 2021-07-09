#!/usr/bin/env python3
# Title : A+B - 3
# Link  : https://www.acmicpc.net/problem/10950

from sys import stdin

# 입력 빠르게 받기
input = stdin.readline

T = int(input())

for _ in range(T):
    print(sum(map(int, input().split())))

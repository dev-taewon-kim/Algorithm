#!/usr/bin/env python3
# Title : 숫자의 합
# Link  : https://www.acmicpc.net/problem/11720

from sys import stdin

# 입력 빠르게 받기
input = stdin.readline

input()
print(sum(map(int, list(input().rstrip()))))

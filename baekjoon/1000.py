#!/usr/bin/env python3
# Title : A+B
# Link  : https://www.acmicpc.net/problem/1000

from sys import stdin

# 입력 빠르게 받기
input = stdin.readline

print(sum(map(int, input().split())))

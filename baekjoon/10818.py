#!/usr/bin/env python3
# Title : 최소, 최대
# Link  : https://www.acmicpc.net/problem/10818

from sys import stdin

# 입력 빠르게 받기
input = stdin.readline

n = int(input())

print((n * (n + 1)) // 2)

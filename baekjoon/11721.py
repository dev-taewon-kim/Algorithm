#!/usr/bin/env python3
# Title : 열 개씩 끊어 출력하기
# Link  : https://www.acmicpc.net/problem/11721

from sys import stdin

# 입력 빠르게 받기
input = stdin.readline

str = input().rstrip()

for i in range((len(str) // 10) + 1):
    if i == 0:
        print(str[:10])
    else:    
        print(str[(i * 10):(i + 1) * 10])

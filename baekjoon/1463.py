#!/usr/bin/env python3
# Title : 1로 만들기
# Link  : https://www.acmicpc.net/problem/1463

from sys import stdin

# 입력 빠르게 받기
input = stdin.readline

n = int(input())

dic = {}

for i in range(1, (10 ** 6) - 1):
    num = i
    count = 0

    while num != 1:
        # 여기에 딕셔너리 검색 로직 넣기
        if num % 3 == 0:
            num //= 3
        elif num % 2 == 0:
            num //= 2
        else:
            num -= 1
        count += 1
    
    dict[num: count]

print(count)

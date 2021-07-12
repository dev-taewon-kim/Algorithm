#!/usr/bin/env python3
# Title : 제곱수의 합
# Link  : https://www.acmicpc.net/problem/1699

from sys import stdin
import math
from itertools import product

# 입력 빠르게 받기
input = stdin.readline

n = int(input())
cnt = 0
result = 0

square_numbers = [i ** 2 for i in range(1, int(math.sqrt(n)) + 1)]

while not result:
    cnt += 1
    for x in product(square_numbers, repeat=cnt):
        if sum(x) == n:
            result = cnt
            break

print(cnt)

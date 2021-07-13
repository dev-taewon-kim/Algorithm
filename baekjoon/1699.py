#!/usr/bin/env python3
# Title : 제곱수의 합
# Link  : https://www.acmicpc.net/problem/1699

from sys import stdin
import math

# 입력 빠르게 받기
input = stdin.readline

n = int(input())

arr = [i for i in range(n + 1)]

for i in range(2, n + 1):
    for j in range(1, int(math.sqrt(i)) + 1):
        if arr[i - (j * j)] + 1 < arr[i]:
            arr[i] = arr[i - (j * j)] + 1

print(arr[n])

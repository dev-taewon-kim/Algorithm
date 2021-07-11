#!/usr/bin/env python3
# Title : 1로 만들기
# Link  : https://www.acmicpc.net/problem/1463

from sys import stdin

# 입력 빠르게 받기
input = stdin.readline

n = int(input())

arr = [0, 0, 1, 1] # 0부터 3까지 각각 1로 만들기 위한 연산의 횟수

for i in range(4, n + 1):
    arr.append(arr[i - 1] + 1)

    if i % 3 == 0 and (arr[i//3] + 1 < arr[i]):
        arr[i] = arr[i//3] + 1
    if i % 2 == 0 and (arr[i//2] + 1 < arr[i]):
        arr[i] = arr[i//2] + 1
    
    # min(arr[i - 1] + 1, arr[i//2] + 1, arr[i//3] + 1)

print(arr[n])

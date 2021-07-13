#!/usr/bin/env python3
# Title : 연속합
# Link  : https://www.acmicpc.net/problem/1912

from sys import stdin

# 입력 빠르게 받기
input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [0] * (n + 1)
dp[0] = arr[0]
result = dp[0]

for i in range(1, n):
    dp[i] = max(dp[i - 1] + arr[i], arr[i])
    result = max(result, dp[i])

print(result)

#!/usr/bin/env python3
# Title : 암호코드
# Link  : https://www.acmicpc.net/problem/2011

from sys import stdin

# 입력 빠르게 받기
input = stdin.readline

arr = list(map(int, list(input().rstrip())))
n = len(arr)
dp = [0] * (n + 1)

if arr[0] == 0:
    print(0)
    quit()

dp[0], dp[1] = 1, 1

for i in range(2, n + 1):
    if not (arr[i - 2] + arr[i - 1]):
        break
    
    if (arr[i - 1]):
        dp[i] = dp[i - 1]

    double_digits = (arr[i - 2] * 10) + arr[i - 1]

    if (10 <= double_digits <= 26):
        dp[i] += dp[i - 2]

print(dp[n] % 1000000)

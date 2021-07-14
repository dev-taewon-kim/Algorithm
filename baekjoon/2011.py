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

dp[0] = 1

for i in range(1, n + 1):
    if (1 <= arr[i - 1] <= 9):
        dp[i] += dp[i-1]
    if i == 1:
        continue

    double_digits = (arr[i - 2] * 10) + arr[i - 1]

    if (10 <= double_digits <= 26):
        dp[i] += dp[i-2]

print(dp[n] % 100000)

# 25114 -> 6
# 2, 5, 1, 1, 4
# 25, 1, 1, 4
# 25, 11, 4
# 25, 1, 14
# 2, 5, 11, 4
# 2, 5, 1, 14


# 12345 -> 3
# 1, 2, 3, 4, 5
# 12, 3, 4, 5
# 1, 23, 4, 5


# 987654321 -> 2
# 9, 8, 7, 6, 5, 4, 3, 2, 1
# 9, 8, 7, 6, 5, 4, 3, 21

# 201912024 -> 3
# 20, 1, 9, 1, 20, 2, 4
# 20, 1, 9, 1, 20, 24
# 20, 19, 1, 20, 24

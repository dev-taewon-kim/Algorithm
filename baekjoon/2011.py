#!/usr/bin/env python3
# Title : 암호코드
# Link  : https://www.acmicpc.net/problem/2011

from sys import stdin

# 입력 빠르게 받기
input = stdin.readline

encrypted = input().rstrip()
n = len(encrypted)
dp = [0] * n

if encrypted[0] == '0':
    result = 0

else:
    for i in range(n):
        if encrypted[i] != '0':
            dp[i] = 1
            if 9 < int(encrypted[i:i + 2]) < 27:
                dp[i] += 1
        else:
            if dp[i - 1] == 2:
                pass
            else:
                print(0)
                quit()


print(dp)

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

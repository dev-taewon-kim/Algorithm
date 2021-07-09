#!/usr/bin/env python3
# Title : 2007년
# Link  : https://www.acmicpc.net/problem/1924

from sys import stdin

# 입력 빠르게 받기
input = stdin.readline

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_the_week = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
calendar = [{} for _ in range(12)]
calendar[0][1] = "MON"

for month in range(12):
    for day in range(days[month]):
        if (month == 0 and day == 0):
            continue
        
        the_day_before = calendar[month][day] if day != 0 else calendar[month - 1][days[month - 1]]
        today_index = day_of_the_week.index(the_day_before) + 1
        today = ""
        
        if today_index > 6:
            today = day_of_the_week[0]
        else:
            today = day_of_the_week[today_index]

        calendar[month][day + 1] = today

month, day = map(int, input().split())
print(calendar[month - 1][day])

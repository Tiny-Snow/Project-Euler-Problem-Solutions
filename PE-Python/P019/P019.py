# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Sat, 6 Feb 2021, 00:12
# Project Euler # 019 Counting Sundays

#==========================================================================Solution
start = 2
end = 0
week_day = start    # 表示星期（不取余）
Sun_days = 0        # 符合的星期日的数目
for year in range(1901, 2001):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        yearday = 366
        leap_month_1st = [
            week_day,
            week_day + 31,
            week_day + 31 + 29,
            week_day + 31 + 29 + 31,
            week_day + 31 + 29 + 31 + 30,
            week_day + 31 + 29 + 31 + 30 + 31,
            week_day + 31 + 29 + 31 + 30 + 31 + 30,
            week_day + 31 + 29 + 31 + 30 + 31 + 30 + 31,
            week_day + 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31,
            week_day + 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30,
            week_day + 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31,
            week_day + 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30]
        for day in range(week_day, week_day + yearday):
            if day in leap_month_1st and day % 7 == 0:
                Sun_days += 1
        week_day += yearday       
    else:
        yearday = 365
        not_leap_month_1st = [
            week_day,
            week_day + 31,
            week_day + 31 + 28,
            week_day + 31 + 28 + 31,
            week_day + 31 + 28 + 31 + 30,
            week_day + 31 + 28 + 31 + 30 + 31,
            week_day + 31 + 28 + 31 + 30 + 31 + 30,
            week_day + 31 + 28 + 31 + 30 + 31 + 30 + 31,
            week_day + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31,
            week_day + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30,
            week_day + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31,
            week_day + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30]
        for day in range(week_day, week_day + yearday):
            if day in not_leap_month_1st and day % 7 == 0:
                Sun_days += 1
        week_day += yearday
print(Sun_days)
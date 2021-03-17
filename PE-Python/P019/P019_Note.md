# Project Euler	Problem 019

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Counting Sundays

You are given the following information, but you may prefer to do some research for yourself.

- 1 Jan 1900 was a Monday.
- Thirty days has September,
  April, June and November.
  All the rest have thirty-one,
  Saving February alone,
  Which has twenty-eight, rain or shine.
  And on leap years, twenty-nine.
- A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?



## Solution

本题就是一个分类计算的问题，下面的代码具有复用性：

```python
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
#==========================================================================Answer
The Answer is 171
```


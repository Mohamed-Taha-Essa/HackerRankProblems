import calendar

# print(calendar.TextCalendar(firstweekday=6).formatyear(2023))
m, d, y = map(int ,input().split())

n =calendar.weekday(y, m, d)
# print(calendar.weekday(y, m, d))
# print(calendar.weekheader(5))
print(calendar.day_name[n].upper())
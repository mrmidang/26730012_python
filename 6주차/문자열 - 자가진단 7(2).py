hour, minute = map(int, input().split())

if hour >= 12:
    am_pm = "PM"
else:
    am_pm = "AM"

if hour >= 13:
    hour -= 12

print(f"{hour:02d} : {minute:02d} {am_pm}")

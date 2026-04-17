a = int(input())

year = 2024
month = 8

month += (a-1)*7
month -= 1

year += month // 12
month = month % 12 +1

print(year, month)
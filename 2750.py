length = int(input())
numbers = []

for _ in range(length):
    numbers.append(int(input()))

sorted_numbers = sorted(numbers)

for i in sorted_numbers:
    print(i)

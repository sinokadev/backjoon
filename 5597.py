students = [False for i in range(30)]

for i in range(28):
    students[int(input())-1] = True

first = students.index(False)
print(first+1)
students.pop(first)
print(students.index(False)+2)
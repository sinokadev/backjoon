def isvps(string):
    count = 0
    for char in string:
        if count < 0:
            return False
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1
        
    return count == 0

for i in range(int(input())):
    print("YES" if isvps(input()) else "NO")
inp = input()

maxlist = [0 for i in range(26)]

for i in inp:
    maxlist[ord(i.upper())-65] += 1

if maxlist.count(max(maxlist)) > 1:
    print("?")
else:
    print(chr(maxlist.index(max(maxlist))+65))

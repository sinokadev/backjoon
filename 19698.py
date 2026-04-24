n, w, h, l = input().split()

print(min(int(n), (int(w)//int(l))*(int(h)//int(l))))
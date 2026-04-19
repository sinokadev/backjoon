a,b,c = map(int, input().split())
aa,bb,cc = map(int, input().split())
max =a*3+b*20+c*2*60
mel =aa*3+bb*20+cc*2*60

if max == mel:
    print("Draw")
elif max < mel:
    print("Mel")
elif max > mel:
    print("Max")
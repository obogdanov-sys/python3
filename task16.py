n = int(input())
for i in range(2, n + 1):
    s = 0
    for d in range(1,i):
        if i%d==0:
            s+=d
    if s==i:
        print(i, end=" ")
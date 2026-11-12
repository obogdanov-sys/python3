x = int(input())
c=0
for a in range(1, x + 1):
    for b in range(a, x + 1):
        if a**2+b**2==x:
           c+=1
print(c)

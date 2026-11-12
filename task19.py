n=int(input())
t=0
for i in range(0,n+1):
    for a in range(i,n+1):
        t+=i+a
print(t)

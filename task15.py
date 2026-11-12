n=int(input())
for i in range(2,n+1):
    c=0
    for d in range(1,i//2+1):
        if i%d==0:
            c+=1
    if c==1:
        print(i)
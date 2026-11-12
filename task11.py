best = -1
while True:
    t=int(input())
    if t==-1:
        break
    if best== -1 or t > best:
        best=t
print(best)
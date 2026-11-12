c = 0
x=None
while True:
    t=float(input())
    if t == 0:
        break
    if x is not None and t < x:
        c+=1
    x=t
print(c)
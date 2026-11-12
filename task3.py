while True:
    N=int(input("Введи число: "))
    if N**0.5==int(N ** 0.5):
        print("полный квадрат")
        break
    else:
        print("не полный квадрат, попробуй ещё")

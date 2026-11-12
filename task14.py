while True:
    t=input("Введите число: ")
    if t.isdigit():
        print(f"Введено целое число: {t}")
        break
    else:
        print("Ошибка. Попробуйте еще раз.")
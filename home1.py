name = input("Введіть ваше ім'я: ")
age = input("Введіть ваш вік: ")
print(f"Привіт {name}, тобі {age}!")
user_age = int(input("Введіть ваш вік: "))
if user_age > 18:
    print("Вхід дозволено")
else:
    print("Вхід заборонено")
    import random

    secret_number = random.randint(1, 10)
    print("Комп'ютер загадав число від 1 до 10. Маєте 3 спроби.")

    for attempt in range(1, 4):
        guess = int(input(f"Спроба {attempt}: "))
        if guess == secret_number:
            print("Вітаємо! Ви вгадали число!")
            break
        elif guess > secret_number:
            print("Менше")
        else:
            print("Більше")
    else:
        print(f"Ви програли. Загадане число було: {secret_number}")
        a = int(input("Введіть число a: "))
        b = int(input("Введіть число b: "))
        for i in range(a, b + 1):
            print(i, end=" ")
        print()
        n = int(input("Введіть число n: "))
        start_num = n if n % 2 == 0 else n - 1
        for i in range(start_num, 0, -2):
            print(i, end=" ")
        print()
        n_fact = int(input("Введіть число n: "))
        factorial = 1
        for i in range(1, n_fact + 1):
            factorial *= i
        print(f"Факторіал числа {n_fact} дорівнює {factorial}")
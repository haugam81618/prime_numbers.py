# Программа для вывода простых чисел

n = int(input("Введите число: "))

# Перебор чисел от 2 до n
for num in range(2, n+1):
    # Проверка на простоту
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=" ")

number = int(input('Введите число: '))

max_number = 0
while number:
    current = number % 10
    number = number // 10

    max_number = current if current > max_number else max_number

print(max_number)
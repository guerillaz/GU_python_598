first_day = int(input('Кол-во километров: '))
end_result = int(input('Результат: '))
day_count = 1

while first_day < end_result:
    day_count = day_count + 1
    first_day = first_day + (first_day * 0.1)
else:
    print (day_count)
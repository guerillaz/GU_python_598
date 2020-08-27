revenue = int(input('Введите сумму прибыли: '))
costs = int(input('Введите сумму издержек: '))

profit = revenue - costs
profitable = profit > 0
if profitable:
    print ('Фирма работает в прибыль')
    workers = int(input('Введите количество работников: '))
else:
    print ('Фирма работает в убыток')

if not profitable:
    exit()

efficiency = profit / revenue
profit_per_head = profit / workers

print(f'Рентабельность {efficiency}')
print(f'Прибыль на человека {profit_per_head}')
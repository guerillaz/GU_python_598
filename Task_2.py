user_seconds = int(input('Введите кол-во секунд: '))

hours = user_seconds // 60 ** 2
minutes = (user_seconds // 60) - (hours * 60)
seconds = user_seconds - (minutes * 60) - (hours * 60 ** 2)

print(f'{hours:0>2}:{minutes:0>2}:{seconds:0>2}')

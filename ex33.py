i = 0

numbers = []

print(i)
while i < 6:
    print('Вверху значение i равно %d' % i)
    numbers.append(i)
    print(i)
    i = i + 1
    print('Текущее значение:', numbers)
    print('Внизу значение i равно %d' % i)
    print(i)

print('Значение:')

for num in numbers:
    print(num)


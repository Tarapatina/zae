def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print('У нас есть %d бутылок лимонада!' % cheese_count)
    print('У нас есть %d коробок чипсов!' % boxes_of_crackers)
    print('Этого достаточно для вечеринки! Поехали! \n')

print('Мы можем непосредственно передать числа функции:' ),cheese_and_crackers(20,30)

print('ИЛИ, мы можем использовать пременные из нашего сценария:')
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print('Мы даже можем выполнять вычисления внутри функции')
cheese_and_crackers(10 + 20, 5 + 6)

print('И объединять переменные с вычислениями: ')
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print('Введите количество лимонада и чипсов')
a = int(input())
b = int(input())
print(cheese_and_crackers(cheese_count=a, boxes_of_crackers=b))



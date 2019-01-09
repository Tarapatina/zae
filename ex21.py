def add(a, b):
    print("Сложение %d + %d" % (a, b))
    return a + b

def subtract (a,b):
    print('Вычитание %d - %d' %(a,b))
    return a - b

def multiply (a,b):
    print('Умножение %d * %d'%(a,b))
    return a * b

def divide (a,b):
    print('Деление %d / %d' %(a, b))
    return a // b

print('Давайте выполним несколько вычислений с помощью функций!')

age = add (30, 7)
height = subtract(190, 4)
weight = multiply(35, 2)
iq = divide(220, 2)

print( "Возраст: %d, рост: %d, вес: %d, IQ %d" % (age, height, weight, iq)) #тут выдает ошибку, хз почему

print('Это головоломка \n')

what = add(age,subtract(height,multiply(weight,divide(iq,2))))

print( "Получается:  ", what, 'Вы можете это вычислить вручную?')


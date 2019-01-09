print('Давайте попрактикуемся!')
print('Вы должны знать об управляющих последовательностях с символом \\, которые \n управляют переносом строк и \t отступами')

poem = """
\t Для счастья
мне совсем немного надо.
Хочу тебя \n я нежно обнимать,
Хочу всегда
я быть с тобою рядом
\n\t\t И никогда тебя не отпускать!"""


print("______________________")
print(poem)
print("______________________")

five = 10-2 + 3-6
print('Здесь должна быть пятерка: %s' % five)

def secret_formula (started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans,jars,crates

started = 10000

beans, jars, crates = secret_formula(started)

print('Начиная с: %d' % started)
print('У нас есть %d бобов, %d банок и %d ящиков'% (beans,jars,crates))
started = started / 10

print('Так же можно поступить следующим образом:')
print(('У нас есть %d бобов, %d банок и %d ящиков.') % secret_formula(started))



x = ' Существует %d типов людей .' % 10
binary = 'Python'
do_not = 'no'
y = 'Те кто понимает %r ,  и те, кто -%s.' % (binary, do_not)

print(x)
print(y)

print('Я сказала: %s' %x)
print('А еще я сказала: %s.' %y)

hilarious = False
joke_evaluation = ("Разве это не смешно? %r")

print(joke_evaluation % hilarious)

w = 'это часть строки слева... '
e = 'а это справа'

print(w + e)
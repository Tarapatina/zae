#  похоже на сценарии с argv

def print_two(*args): # *args -это произвольное число аргументов
    arg1, arg2 = args
    print('arg1: %r, arg2: %r' % (arg1, arg2))


# Ок тут вместо *args мы делаем следующее
def print_two_again(arg1, arg2):
    print('arg1: %r, arg2: %r' % (arg1, arg2))


# принимает только один аргумент
def print_one(arg1):
    print('arg1: %r' % arg1)


# не принимает аргументов
def print_none():
    print('А я ничего не получаю')

print_two('Zed','Shaw')
print_two_again('Zed','Shaw')
print_one('First')
print_none()


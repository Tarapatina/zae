from sys import argv

script, input_file = argv, 'new.txt'

def print_all (f):
    print(f.read())

def rewind(f):
    f.seek(0) # каждый раз когда выполняем seek мы двигаемся к началу файла

def print_a_line(line_count, f):
    print(line_count, f.readline()) # считывается одна строка из файла

current_file = open(input_file)

print('Первым делом выведем этот файл целиком: \n')

print_all(current_file)

print('Теперь отмотаем назад, словно это кассета')

rewind(current_file)
print('И выведем три строки:')
rewind(current_file)
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)

current_line = current_line +1
print_a_line(current_line,current_file)



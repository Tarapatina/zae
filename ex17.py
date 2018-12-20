from sys import argv
from os.path import exists # импорт функции exists, она возвращает True, если файл существует,
# основываясь на его имени, указываемом в качестве аргумента. Или же False, если его нету

script, from_file, to_file = argv, 'ex15_sample.txt', 'new.txt'

print('Копирование данных из файла %s в файл %s'% (from_file, to_file))

indata = open(from_file).read()

print('Исходный файл имеет размер %d байт' % len(indata))# длина строки

print('Файл назначения существует? %r' % exists(to_file))

print('Готов к работе, нажмите клавишу Enter для продолжения или клавишу Ctrl+C для отмены')
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print('Отлично, все сделанно...')

out_file.close()




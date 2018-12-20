# _*_ coding: utf- 8 _*_

import codecs,sys
#outf = codecs.getwriter('cp866')(sys.stdout, errors = 'replace')

#sys.stdout = outf

from sys import argv

script, filename = argv, 'ex15_sample.txt'

print('Я собираюсь стереть файл %r' % filename)
print('Если вы не хотите стирать его, нажмите сочетание клавиш CTRL+C (^C)')
print('Если хотите стереть файл, нажмите клавишу Enter')

input('?')

print('Открытие файла....')
target = open (filename,'w')

print('Очистка файла. До свидания!')
target.truncate()

print("Теперь я запрашиваю у вас три строки")

line1 = input('Cтрока 1:')
line2 = input('Cтрока 2:')
line3 = input('Cтрока 3:')

print("Это я запишу в файл")

target.write(line1 +'\n'+ line2 +'\n' +line3+'\n')

# target.write(line1)
# target.write('\n')
# target.write(line2)
# target.write('\n')
# target.write(line3)
# target.write('\n')

print('И наконец я закрою файл')
target.close()


txt = open(filename) #открывает нужный файл

print('Содержимое файла: %s' % filename)

print(txt.read()) # читает наш файл
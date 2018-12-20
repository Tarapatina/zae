from sys import argv

script, filename = argv, 'ex15_sample.txt'

txt = open(filename) #открывает нужный файл

print('Содержимое файла: %s' % filename)

print(txt.read()) # читает наш файл
txt.close() # закрыват наш файл

print('Введите имя файла снова:')
file_again = input('> ')


txt_again = open(file_again) # открывает опять наш файл

print(txt_again.read()) # читает его

txt_again.close() # и закрывает


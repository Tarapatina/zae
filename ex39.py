
countries ={
    'Россия': 'RU',
    'Германия': 'DE',
    'Узбекистан':'UZ',
    'Зимбабве':'ZW',
    'Турция':'TR'
}

#cоздание базового набора стран и некоторых городов в них
cities ={
    'UZ':'Газли',
    'TR':'Сарыгерме',
    'DE':'Мюнхен'
}

#добавление некоторых городов

cities['ZW'] = 'Гверу'
cities['RU'] = 'Москва'

#вывод некоторых городов
print("- "*10)
print('В стране ZW есть город:',cities['ZW'])
print('В стране RU есть город:',cities['RU'])

# вывод некоторых стран
print('- '*10)
print('Аббревиатура Турции:',countries['Турция'])
print('Аббревиатура Германии:',countries['Германия'])

# выполняется с учетом страны и словаря городов
print('- '*10)
print('В Турции есть город:', cities[countries['Турция']])
print('В Германии есть город:', cities[countries['Германия']])


# вывод аббревиатур всех стран
print('- '*10)
for country, abbrev in countries.items(): # .items-возвращает пары (ключ, значение).
    print('%s имеет аббревиатуру %s'%(country,abbrev))

#вывод всех городов в странах
print('- '*10)
for abbrev,city in cities.items(): # .items() - возвращает пары (ключ, значение).
    print('В стране %s есть город %s' % (abbrev,city))

#  а теперь сразу оба типа данных
print('- '*10)
for country, abbrev in countries.items(): #.items() - возвращает пары (ключ, значение).
    print('в стране %s используется аббревиатура %s и есть город %s'%(country,abbrev,cities[abbrev]))

print('- '*10)
# беззопасное получение аббревиатуры страны, которая не представлена
country = countries.get('США', None)

if not country:
    print('Прошу прощения, США не обнаружено')

# получение города со значением по умолчанию
city = cities.get('US', 'Не существует')
print("В стране 'US' есть город:%s" % city )


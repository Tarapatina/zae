ten_things = 'Apples Oranges Crows Telephone Light Sugar'
print(ten_things)

print('Погодите, тут меньше 10 объектов. Давайте испраивм это?')

stuff = ten_things.split(' ') # метод split() возвращает список всех слов в строке
more_staff = ['day', 'Night', 'Song', 'Frisbee', 'Corn', 'Banana', 'Girl','Boy']# список
print(more_staff)

while len(stuff) != 10:
    next_one = more_staff.pop() # берем последний элемент в нашем списке
    print('Добавляем:', next_one)# добавляем последний элемент, взятый со списка
    stuff.append(next_one) # добавляет элемент в конец списка
    print(more_staff)
    print('Теперь у нас %d объектов. ' % len(stuff))

print('И так:',stuff)

print('Давайте кое-что сделаем с нашими объектами')

print (stuff[1])
print(stuff[-1])
print(stuff.pop())# берем последний элемент в нашем списке, в нашем случае Corn
print(' '.join(stuff)) # c помощью джоин, выводится весь список через пробел

print('#'.join(stuff[3:5]))# выводится наш срез списка с #
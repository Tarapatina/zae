# -*- coding: utf-8 -*-
import ex23
def break_words(stuff):
    """Эта функция разбирает текст на слова."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Сортирует слова."""
    return sorted(words)

def print_first_word(words):
    """Выводит первое слово после извлечения."""
    word = words.pop(0)
    print (word)

def print_last_word(words):
    """Выводит последнее слово после извлечения."""
    word = words.pop(-1)
    print (word)

def sort_sentence(sentence):
    """Принимает целое предложение и возвращает отсортированные слова."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Выводит первое и последнее слова предложения."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Сортирует слова, а затем выводит первое и последнее."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print ("Давайте попрактикуемся!")
print ('Вы должны знать об управляющих последовательностях с символом \\, которые \n управляют переносом строк и \t отступами.')

poem = u"""
\tДля счастья
мне совсем немного надо.
Хочу тебя \n я нежно обнимать,
Хочу всегда
я быть с тобою рядом
\n\t\tИ никогда не отпускать!
"""


print ("--------------")
print (poem)
print ("--------------")

five = 10 - 2 + 3 - 6
print ("Здесь должна быть пятерка: %s" % five)

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print ("Начиная с: %d" % start_point)
print ("У нас есть %d бобов, %d банок и %d ящиков." % (beans, jars, crates))

start_point = start_point / 10

print ("Также можно поступить следующим образом:")
print ("У нас есть %d бобов, %d банок и %d коробок." % secret_formula(start_point))


sentence = "All god\t things come to those who weight."

words = ex23.break_words(sentence)
sorted_words = ex23.sort_words(words)

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words)
print_last_word(sorted_words)
sorted_words = ex23.sort_sentence(sentence)
print (sorted_words)

print_first_and_last(sentence)

print_first_and_last_sorted(sentence)


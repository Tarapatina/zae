import codecs, sys


from sys import argv

script, user_name =' 1', 'Katty'
prompt = '>'

print('Привет %s, Я - сценарий %r.' % (user_name, script))
print('Я хочу задать тебе несколько вопросов')
print("Я тебе нравлюсь , %s?" % user_name)
likes = input()

print("Где ты живешь, %s?" % user_name)
lives = input()

print('На каком компе ты работаешь?')
comp = input()

print("""
И так, ты ответил %r на вопрос, нравлюсь ли я тебе.
Ты живешь в %r. Не представляю где это.
И у тебя есть комп %r. Чудесно!
""" % (likes,lives, comp))















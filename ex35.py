import codecs, sys
#outf = codecs.getwriter('cp866')(sys.stdout, errors ='replace')
#sys.stdout = outf

from sys import exit

def gold_room():
    print('Здесь полно золота! Сколько кг ты унесешь?')

    next = input('>')

    if '0' in next or '1' in next:# зачем тут нужно цифры приравнивать к 1 или о? а если я хочу ввести 25?
        how_much = int()
    else:
        dead('Эй, ввести надо число!')


    if how_much < 50:
        print('Шикарно! Ты не жадный, поэтому выигрываешь!')
        exit(0)

    else:
        dead ('Ах ты жадина!')

def bear_room():
    print('Здесь сидит медведь')
    print('у медведя бочка с медом')
    print('Медведь закрыл собой дверь выхода')
    print('Ка переместить медведя? отобрать мед или подразнить медведя?')

    bear_moved = False

    while True:
        next = input('>')

        if next == 'отобрать мед'or next=='Отобрать мед':
            dead('Медведь посмотрел на тебя и ударил лапой по лицу.')
        elif next == 'подразнить медведя' and not bear_moved:
            print('Медведь отошел от двери. Вы можете войти в нее. Подразнить медведя или войти в дверь?')
            bear_moved = True
        elif next == 'подразнить медведя' and bear_moved:
            dead('Медведь разозлился и откусил тебе ногу')
        elif next == 'войти в дверь' and bear_moved:
            gold_room()
        else:
            print('Понятия не имею, что происходит')

def cthulhu_room():
    print('На вас смотрит великий и ужасный Ктулху')
    print("Он смотрит на тебя, и ты начинаешь сходить с ума")
    print("Убежать или съесть свою голову?")

    next = input('>')

    if 'убежать' in next:
        start()
    elif 'съесть свою голову' in next:
        dead('Хм, а это даже и вкусно!')

    else:
        cthulhu_room()


def dead(why):
    print(why, 'Великолепно!')
    exit(1)

def start():
    print('ты в темной комнате')
    print("отсюда ведут две двери, налево и направо")
    print("Куда ты повернешь?")


    next = input('>')

    if next == 'налево':
        bear_room()
    elif next == 'направо':
        cthulhu_room()
    else:
        dead('ты ходишь из комнаты в комнату,пока не умираешь с голоду')

start()
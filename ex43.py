import codecs, sys

from sys import exit
from random import randint

class Scene (object): # базовый Класс, который будет включать общие элементы для всех сцен в игре

    def enter (self):
        print('Эта сцена еще не настроена. Создайте подкласс и реализуйте функцию enter()')
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play (self):
        current_scene = self.scene_map.opening_scene()

        while current_scene!= last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene (next_scene_name)

class Death (Scene):

    quips = [
        'Вы погибли. Как это ни печально.',
        'Ваша мать будет грустить по вам...надо было быть умнее',
        'Надо же было быть таким придурком',
        'Даже мой маленький щенок соображдает лучше'
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor (Scene):

    def enter(self):
        print('Готоны с планеты Перкаль 25 захватили ваш корабль и уничтожили')
        print(" Всю команду.; Вы - единственный, кто остался в живых")
        print("Вам нужно выкрасть нейтронную бомбу в оружейной лаборатории,")
        print("Заложить ее в топлевном отсеке и покинуть корабль в спасательной ")
        print("капсуле прежде, чем он взорвется")
        print('\n')
        print('Вы бежите по центральному коридору в оружейную лабораторию, когда перед вами')
        print("появляется Готон с красной чешуйчатой кожей, гнилыми зубами и в костюме клоуна")
        print("Он с ненавистью смотрит на вас и, преградив дорогу в лабораторию,")
        print(" вытаскивает бластер, чтобы уничтожить вас.")

        action = input('>')

        if action == 'cтрелять!':
            print("Вы быстро выхватываете свой бластер и начинаете палить по Готону.")
            print("Его клоунский наряд крутится и мешает лучам попадать в")
            print("его тело. Все ваши выстрелы лазеромпотерпели неудачу, и заряд бластре иссяк")
            print("Костюм Готона, который купила его мать, безнадежно испорчен, поэтому")
            print("он в ярости выхватывает бластер и стреляет вам в голву")
            print("Вы убиты")
            return 'death'

        elif action == 'проскочить!':
            print('Словно боксер мирового класса, вы уворачиваетесь и проскальзываете справа ')
            print('от Готона, краем глаза видя, что его бластер направлен вам в голову.')
            print('И тут вы подскальзываетесь и врезаетесь в металлическую стену. От удара')
            print('вы теряете сознание.')
            print('Придя в сознание, вы успеваете почувствовать, что Готон топчется на вашей')
            print('голове и пожирает вас')
            return 'death'

        elif action == 'пошутить!':
            print('К счастью, вы знакомы с культурой Готонов и знаете, что их способно рассмешить ')
            print("Вы рассказываете  бородатый анекдот:")
            print("Неоколонии, изоморфно релятивные к мультиполосным гиперболическим параболоидам.")
            print("Готон замирает, старается сдержать смех, а затем начинает безудержно хохотать")
            print("Пока он смеется, вы достаете бластер и стреляете Готону в голову")
            print("Он падает, а вы перепрыгиваете его и бежите в оружейную лабораторию")
            return 'laser_weapon_armory'
        else:
            print('ТАК НЕЛЬЗЯ ПОСТУПИТЬ!')
            return 'central_corridor'


class LaserweaponArmory(Scene):

    def enter(self):
        print('Вы вбегаете в оружейную лабораторию и начинаете обыскивать комнату,')
        print("спрятались ли тут другие Готаны. Стоит мертвая тишина.")
        print("Вы бежите в дальний угол комнаты и находите нейтронную бомбу")
        print("в защитном контейнере. На лицевой стороне контейнера расположена")
        print("панель с кнопками, и вам надо ввести правильный код, чтобы достать бомбу")
        print("Если вы 10 раз введете неправильный код, контейнер заблокируется, и вы")
        print("не  сможете достать бомбу. Код состоит из трех цифр")

        code = '%d %d %d' % (randint(1,9), randint(1,9), randint(1,9))

    quess =input('[keypad]>')
    quesses = 0

    while quess != code and quesses <10:
        print('ВЖЖЖЖЖИИИИККК!')
        quesses += 1
        quess = input('[keypad]>')

    if guess == code:
        print('Контейнер открвается  со щелчком и выпускает сизый газ.')
        print("Вы вытаскиваете нейтронную бомбу и бежите в топливный отсек,")
        print("чтобы установить бомбу в нужном месте")
        return 'the_fuelcell'
    else:
        print('Вы слышите, как замок жужжит  последний раз, а затем чувствуете')
        print("горелый запах -замок расплавился")
        print("Вы остаетесть в оружейной лавке, пока наконец Готоны не взорвут")
        print("ваш корабль со своего и вы не умрете")
        return 'death'

class TheFuelcell (Scene):

    def enter(self):
        print('Вы вбегаете в топливный отсек с нейтронной бомбой и видите')
        print("пятерых Готонов, безуспешно пытающихся управлять ")
        print("кораблем. Один уродливее другого, и все в клоунских")
        print("костюмах, как и Готон, убитый вами. Они не достают оружие,")
        print("так как видят у вас бомбу в руках и не хотят чтобы вы установили ее")

        action = input('>')

        if action == 'бросить бомбу':
            print("Вы в панике активируете и бросаете бомбу в толпу Готонов,")
            print("а затем прыгаете к двери шлюза. Сразу после этого")
            print("один из Готонов стреляет вам в спину. Умирая,")
            print("вы видите, как другие Готоны тщетно пытаются деактивировать ")
            print("бомбу. Умирая, вы осознаетек, что Готоны тоже погибнут")
            print(" Ваше сознание угасает")
            return 'death'

        elif action =='установить бомбу':
            print('Вы указываете бластером на бомбу в ваших руках. Готоны поднимают лапы ввкерх и в страхе потеют.'
                  'Вы осторожно, не отворачиваясь, подходите к двери и аккуратно устанавливаете бомбу, держа Готонов под прицелом'
                  'Вы запрыгиваете в шлюз и закрываете его ударом по кнопке, а заьтем бластером расправляете замок, чтобы Готоны не смогли открыть дверь.'
                  'Теперь вам нужно залезть в спасательную капсулу и удрать с корабля к черям собачьим'
                  )
            return 'escape_pod'
        else:
            print('ТАК НЕЛЬЗЯ ПОСТУПАТЬ!')
            return 'the_fuelcell'


class EscapePod (Scene):

    def enter(self):
        print('Вы мчите по отсеку со спасательными капсулами. Некоторые из них могут быть повреждены'
              'и взорвуться во время полета. всего капсул 5, и у вас нет времени , чтоб осматривать каждую из них'
              'на отсутствие повреждений. Задумавшись на секунду, вы решаете сесть в капсулу под номером ....'
              'Какой номер вы выбираете?')
        good_pod = randint(1,5)
        guess = input('[pod#]>')


        if int(guess) != good_pod:
            print('Вы запрыгиваете в капсулу № %s и нажимаете кнопку отстыковки.' % guess)
            print('капсула вылетает в космическое пространство, а затем взрывается с яркой вспышкой и разбрасывая осколки. Вы умираете')
            return 'death'

        else:
            print('Вы запрыгиваете в капсулу № %s и нажимаете кнопку отсастыковки' % guess)
            print(" Капсула вылетает в космическиое пространство, а затем отправляется к планете неподалеку. Вы смотрите "
                  "в иллюминатор и видите как ваш корабль взрывается. "
                  "Его осколки осколки повреждают топливный отсек корабля Готонов, и тот тоже разрывается. Победа!")

            return 'finished'

class Finished (Scene):

    def enter(self):
        print('Вы победили! Отличная работа!')
        return 'finished'

class Map(object):

    scenes = [
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserweaponArmory(),
        'the_fuelcell': TheFuelcell(),
        'escape_pod': EscapePod(),
        'death':Death(),
        'finished': Finished(),
    ]

def __init__(self,start_scene):
    self.start_scene = start_scene

def next_scene(self, start_name): val = Map.scenes.get (scene_name)
    return val

def opening_scene(self):
    return self.next_scene (self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
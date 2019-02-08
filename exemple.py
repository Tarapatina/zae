def gold_room():
    print('Здесь полно золота! Сколько кг ты унесешь?')

    next = input('>')

    if '0' in next or '1' in next:
        how_much = int(next)
    else:
        dead('Эй, ввести надо число!')

    if how_much < 50:
        print('Шикарно! Ты не жадный, поэтому выигрываешь!')
        exit(0)

    else:
        dead ('Ах ты жадина!')

def dead(why):
    print(why, 'Великолепно!')
    exit(0)

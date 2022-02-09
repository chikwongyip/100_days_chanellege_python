from ast import While
from random import randint
money = 1000

while money > 0:
    print(f'你的总资产为：{money}元')
    go_on = False

    while True:
        debt = int(input('请下注:'))
        if 0 < debt <= money:
            break
    
    first = randint(1,6) + randint(1,6)
    print(f'\n玩家摇出了{first}点')
    if first == 7 or first == 11:
        print('You win')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('You lost')
    else:
        go_on = True
    
    while go_on:
        go_on = False
        current = randint(1,6) + randint(1,6)
        print(f'玩家摇出了{current}点')

        if current == 7:
            print('You lost')
            money -= debt
        elif current == first:
            print('You WIN')
            money += debt
        else:
            go_on = True
print('你破产了，游戏结束')


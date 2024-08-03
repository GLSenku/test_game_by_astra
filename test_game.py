from test_gamedata import *
from test_gamefunc import *
name = input("Кто ты, воин?")
player["name"] = name
current_enemy = 0

while True:
    action = input('''
        1 - Бой
        2 - Тренировка
        3 - Магазин
        4 - Отобразить инвентарь
        5 - Заработать денег
        6 - Отобразить игрока
        Exit - Выход из игры
''')
    if action == "1":
        fight(current_enemy)
    elif action == '2':
        training_type = input('''
            1 - Тренировка атаки
            2 - Тренировка защиты
''')
        training(training_type)
    elif action == '3':
        shop()
    elif action == '4':
        display_inventory()
    elif action == '5':
        earn()
    elif action == '6':
        display_player()
    elif action == 'Exit':
        break
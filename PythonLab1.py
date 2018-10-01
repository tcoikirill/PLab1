steps_gender = int(input('1. Мужчина \n2. Женщина\n'))
if steps_gender == 1: 
    print('Выбран Мужской шаг')
    step = 0.8
elif steps_gender == 2:
    print('Выбран Женский шаг')
    step = 0.5

steps_num = float(input('Сколько шагов вы сделали? '))
steps_time = float(input('Какое время вы шли? (В минутах) ')) / 60

V = step * steps_num / 1000 / steps_time 

print("%.1f" % V)
if 2 <= V < 4:
    print('Побольше ходи!!!')
elif 4 <= V < 6:
    print('Продолжай в том же духе!')
elif 6 <= V <= 10:
    print('А ты герой!')
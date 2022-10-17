things = {'в': (3, 25), 'п': (2, 15), 'б': (2, 15), 'а': (2, 20), 'и': (1, 5), 'н': (1, 15), 'т': (3, 20), 'о': (1, 25),
          'ф': (1, 15), 'д': (1, 10), 'к': (2, 20), 'р': (2, 20)}

area = [things[i][0] for i in things]  # Список веса предмеов
value = [things[i][1] for i in things]  # Список ценностей предметов
s = [[0 for j in range(9 + 1)] for i in range(len(things) + 1)]  # Пустая таблица из 0
for i in range(1, len(things) + 1):  # Цикл заполнения таблицы по правилу
    for j in range(1, 9 + 1):
        if area[i - 1] <= j:
            s[i][j] = max(s[i - 1][j], s[i - 1][j - area[i - 1]] + value[i - 1])
        else:
            s[i][j] = s[i - 1][j]

res = s[len(things)][9]
j = 9
spis = []
for i in range(len(things), 0, -1):  # Обратный цикл записи ценности и веса нужных предметов
    if res <= 0:
        break
    elif res == s[i - 1][j]:
        continue
    else:
        spis.append((area[i - 1], value[i - 1]))
        res -= value[i - 1]
        j -= area[i - 1]

ans = []
error = ''
for search in spis:  # Поиск нужных предметов в словаре и запись в ans
    for key, val in things.items():
        if val == search and key not in error:
            ans.append(key)
            error += key

value_ans = s[len(things)][9] - (sum(value) - s[len(things)][9]) + 15  # Вычисление итоговых очков выживания

ans_list = []
for i in ans:  # Цикл загонки в двумерный массив
    for j in range(things[i][0]):
        ans_list.append(list(i))
print(ans_list)
print('Итоговые очки выживания:', value_ans)

# Завдання 2 Перемістити елемент у списку
#
# Ваша програма має перенести останній елемент списку з кінця на початок, тобто,
# останній елемент списку має стати першим.
# Послідовність інших елементів не має змінюватися.
#
# Порожній список або список з одним елементом повинен залишитися незмінним.
#
# Кількість елементів у списку може бути будь-яким – нуль та більше!
#
# Приклади:
#
# [12, 3, 4, 10] => [10, 12, 3, 4]
# [1] => [1]
# [] => []
# [12, 3, 4, 10, 8] => [8, 12, 3, 4, 10]

# Для перевірки коректності роботи Вашого коду використовуйте приклади вище.
# Робити запит на введення даних від користувача не потрібно.


value_list = [12, 3, 4, 10, 8]

if len(value_list) > 1:
    value_list.insert(0, value_list.pop())

print(value_list)
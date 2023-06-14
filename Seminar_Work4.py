"""
Задание №1
Погружение в Python | Функции
✔ Напишите функцию, которая принимает строку текста.
Вывести функцией каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого
длинного слова был один пробел между ним и номером строки.
"""


def show_string(text: str) -> [str]:
    str_list = sorted(text.split())
    len_max = len(max(str_list, key=len))
    for i, s in enumerate(str_list, start=1):
        print(f'{i} - {s:>{len_max}}')


# show_string('Привет, как дела?')

"""
Задание №2
✔ Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию.
"""


def uni_code(text: str) -> list[int]:
    return sorted([ord(i) for i in set(text)], reverse=True)


# print(uni_code('Привет, как дела?'))
"""
Задание №3
✔ Функция получает на вход строку из двух чисел через пробел.
✔ Сформируйте словарь, где ключом будет
символ из Unicode, а значением — целое число.
✔ Диапазон пар ключ-значение от наименьшего из введённых
пользователем чисел до наибольшего включительно.
"""


# def convert_text(text: str) -> dict[int]:
#     res ={}
#     k,v = text.split(' ')
#     res[ord(k)] = int(v)
#     return res
#
#
# print(convert_text('2 2'))


def dict_char_num(text: str) -> dict[str:int]:
    minimum, maximum = sorted([int(i) for i in text.split()])
    return {chr(i): i for i in range(minimum, maximum + 1)}


# print(dict_char_num('501 626'))
"""
Задание №4
✔ Функция получает на вход список чисел.
✔ Отсортируйте его элементы in place без использования
встроенных в язык сортировок.
✔ Как вариант напишите сортировку пузырьком.
Её описание есть в википедии.

"""


def bubble_sort(numbers: list[int]) -> list[int]:
    length = len(numbers)
    for i in range(length):
        for j in range(length - 1 - i):
            if numbers[j + 1] < numbers[j]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


# print(bubble_sort([2, 1, 3, 5, 4, 6, 7]))

"""
Задание №5
✔ Функция принимает на вход три списка одинаковой длины:
✔ имена str,
✔ ставка int,
✔ премия str с указанием процентов вида «10.25%».
✔ Вернуть словарь с именем в качестве ключа и суммой
премии в качестве значения.
✔ Сумма рассчитывается как ставка умноженная на процент премии. 
"""


def premium(names: list[str], salary: list[int], bonus: list[str]) -> dict[str:float]:
    return {name: salary / 100 * bonus
            for name, salary, bonus in zip(names, salary, (float(i[:-1]) for i in bonus))}


print(premium(['Вася', 'Петя', 'Коля'], [10000, 20000, 30000], ['12.5%', '15%', '10%']))
"""
Задание №6
✔ Функция получает на вход список чисел и два индекса.
✔ Вернуть сумму чисел между между переданными индексами.
✔ Если индекс выходит за пределы списка, сумма считается
до конца и/или начала списка.
"""


def list_sum(numbers: list[int], index_1: int, index_2: int) -> int:
    index_1 = index_1 if index_1 >= 0 else 0
    index_2 = index_2 if index_2 <= len(numbers) else len(numbers)
    result = 0
    for i in numbers[index_1:index_2]:
        result += i
    return result
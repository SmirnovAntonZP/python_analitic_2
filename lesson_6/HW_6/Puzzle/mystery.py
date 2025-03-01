"""
Модуль отгадывания загадок
"""
__all__ = ['solution', 'get_dict', 'save', 'view']

# 4. Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.

_private_dict = {}


def solution(mystery_str: str, variant_solution: list, attempts: int = 3):
    """
    Функция отгадывания загадки

    :param mystery_str: загадка
    :param variant_solution: варианты ответов
    :param attempts: количество попыток
    :return: возвращаем номер попытки с которой угадали загадку
    """
    print(f'Угадайте загадку: {mystery_str}. У вас есть {attempts} попытки.')
    for i in range(attempts):
        answer = input('Ваш ответ: ').lower()
        for item in variant_solution:
            if answer == item.lower():
                print("Ура, загадка разгадана!")
                return i + 1
        else:
            print(f'У вас осталось {attempts - i - 1} попыток')
    return 0


# 5. Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.
def get_dict() -> dict:
    """
    Функция выдает словарь загадок и ответов.

    :return: загадки и ответы
    """
    return {'Зимой и летом, одним цветом': ['Елка', 'Сосна', 'Пихта'],
            'Без окон и дверей, полна горница людей': ['Огурец', 'огурчик']}


# 6. Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число
# (номер попытки, с которой она угадана).
# Функция формирует словарь с информацией о результатах отгадывания.
# Для хранения используйте защищённый словарь уровня модуля.
# Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде.
# Для формирования результатов используйте генераторное выражение.


def save(mystery_str: str, attempts_ok: int):
    """
    Функция сохраняет результаты отгадывания.

    :param mystery_str: загадка
    :param attempts_ok: номер удачной попытки
    """
    _private_dict[mystery_str] = attempts_ok


def view():
    """
    Функция вывода результатов отгадывания
    """
    print('\n    СТАТИСТИКА')
    if _private_dict != {}:
        max_len_mystery = max(len(key) for key in _private_dict.keys())
        print(*(f'\n{key: <{max_len_mystery}} - {value: <2}' for key, value in _private_dict.items()))
    else:
        print('Ничего не угадали (')


if __name__ == '__main__':
    for mystery_str_, variant_solution_ in get_dict().items():
        n_answer = solution(mystery_str_, variant_solution_)
        if n_answer > 0:
            save(mystery_str_, n_answer)
    view()
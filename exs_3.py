"""
3. Создать два списка с различным количеством элементов. В первом должны быть записаны ключи,
во втором — значения. Необходимо написать функцию, создающую из данных ключей и значений
словарь. Если ключу не хватает значения, в словаре для него должно сохраняться значение None.
Значения, которым не хватило ключей, необходимо отбросить.
"""

FIST_LIST = ["a", "b", "c", "d", "e"]
SECONDARY_LIST = ["1", "2", "3"]
RESULT_DICTIONARY = {}


def create_dictianary(fist_list, secondary_list):
    """
    Создание словаря
    """
    for item_i, value_i in enumerate(fist_list):
        try:
            value_j = secondary_list[item_i]
        except IndexError:
            value_j = 'None'

        RESULT_DICTIONARY[value_i] = value_j

    return RESULT_DICTIONARY


if __name__ == '__main__':
    print(create_dictianary(FIST_LIST, SECONDARY_LIST))

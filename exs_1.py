'''
Вывод таблицы умножения
'''


def multiplication(first_multiplier, secondary_multiplier):
    '''
    Генератор таблицы
    '''
    columns = []
    for i in range(1, first_multiplier + 1):
        for j in range(1, secondary_multiplier + 1):
            columns.append([i, j])

    return columns


def gen_table(row_content):
    '''
    Генератор вывода таблиц
    '''
    return (lambda x: print(f'{x[0]} x {x[1]}'))(row_content)


FIRST_M = None
SECONDARY_M = None

if __name__ == '__main__':
    while True:
        try:
            FIRST_M = int(input("Введите первый множитель: "))
            break
        except ValueError:
            print("Введите натуральное число.")

    while True:
        try:
            SECONDARY_M = int(input("Введите второй множитель: "))
            break
        except ValueError:
            print("Введите натуральное число.")

    for row in multiplication(FIRST_M, SECONDARY_M):
        gen_table(row)

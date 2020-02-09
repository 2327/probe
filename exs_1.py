'''
Вывод таблицы умножения
'''


def multiplication(FIRSTM, SECONDARYM):
    '''
    Генератор таблицы
    '''
    columns = []
    for i in range(1, FIRSTM + 1):
        for j in range(1, SECONDARYM + 1):
            columns.append([i, j])

    return columns


def gen_table(row):
    '''
    Генератор вывода таблиц
    '''
    return (lambda x: print(f'{x[0]} x {x[1]}'))(row)


FIRSTM = None
SECONDARYM = None

if __name__ == '__main__':
    while True:
        try:
            FIRSTM = int(input("Введите первый множитель: "))
            break
        except ValueError:
            print("Введите натуральное число.")

    while True:
        try:
            SECONDARYM = int(input("Введите второй множитель: "))
            break
        except ValueError:
            print("Введите натуральное число.")

    for row in multiplication(FIRSTM, SECONDARYM):
        gen_table(row)



def multiplication(a, b):
    columns = []
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            columns.append([i,j])

    return columns


def gen_table(i):
    return ((lambda x: print(f'{x[0]} x {x[1]}'))(i))


if __name__ == '__main__':
    while True:
        a = input("Введите первый множитель: ")
        try:
            a = int(a)
            break
        except ValueError:
            print("Введите натуральное число.")

    while True:
        b = input("Введите второй множитель: ")
        try:
            b = int(b)
            break
        except ValueError:
            print("Введите натуральное число.")

    for i in multiplication(a, b):
        gen_table(i)


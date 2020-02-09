



def multiplication(a, b):
    columns = []
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            columns.append([i,j])

    return columns

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

    lambda f: (for i in multiplication(a, b) : print(i))


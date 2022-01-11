size = eval(input('size of the board'))
position = lambda a, b: size * a + b
line = lambda a: a // size
column = lambda a: a % size
occupied = list()


def move(i):
    occupied.append(i)
    print('this is {},{}'.format(line(i), column(i)))
    if len(occupied) == size ** 2:
        path()
        return 0
    # 11
    if line(i) - 2 >= 0 and column(i) - 1 >= 0 and (i - 2 * size - 1) not in occupied:
        move(i - 2 * size - 1)
    # 1
    if line(i) - 2 >= 0 and column(i) + 1 <= size - 1 and (i - 2 * size + 1) not in occupied:
        move(i - 2 * size + 1)
    # 7
    if line(i) + 2 <= size - 1 and column(i) - 1 >= 0 and (i + 2 * size - 1) not in occupied:
        move(i + 2 * size - 1)
    # 5
    if line(i) + 2 <= size - 1 and column(i) + 1 <= size - 1 and (i + 2 * size + 1) not in occupied:
        move(i + 2 * size + 1)
    # 10
    if line(i) - 1 >= 0 and column(i) - 2 <= 0 and (i - size - 2) not in occupied:
        move(i - size - 2)
    # 2
    if line(i) - 1 >= 0 and column(i) + 2 <= size - 1 and (i - size + 2) not in occupied:
        move(i - size + 2)
    # 8
    if line(i) + 1 <= size - 1 and column(i) - 2 >= 0 and (i + size - 2) not in occupied:
        move(i + size - 2)
    # 4
    if line(i) + 1 <= size - 1 and column(i) + 2 <= size - 1 and (i + size + 2) not in occupied:
        move(i + size + 2)
    print('back in {},{}'.format(line(i), column(i)))
    # occupied.pop(len(occupied))


def path():
    print('path:', end='')
    for i in occupied:
        print('{},{}->'.format(line(i), column(i)), end='')
    print()
    print(sorted(occupied))


move(0)

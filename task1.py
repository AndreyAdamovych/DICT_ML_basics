def foo(x1, y1, x2, y2):
    k = (y2 - y1) / (x2 - x1)
    b = y1 - x1 * k
    print(f'y = {k}*x', end='')
    print(f'+{b}' if b > 0 else f'{b}')


foo(1, 2, 2, 0)
foo(1, -1, 4, 0)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
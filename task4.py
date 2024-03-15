from collections import deque


def f1():
    with open('history_mirror.txt', encoding='utf8') as f:
        f = f.read()
        res = sorted([x.split('=') for x in f.split('\n')][1:], key=lambda x: x[-1])

    a = deque()

    for x in res:
        if x[-1] == 'Изменение характера':
            print('a')
        elif x[-1] == 'Признание своей уникальности' and len(a) > 0:
            a.pop()

    print(len(a))


f1()

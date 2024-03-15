def find_user(m, name):
    for x in m:
        if name in x[1]:
            return f'Предсказание для {x[1]} - {x[2]}'

    return 'Вы не использовали зеркало'


def f1():
    with open('history_mirror.txt', encoding='utf8') as f:
        f = f.read()
        res = sorted([x.split('=') for x in f.split('\n')][1:], key=lambda x: x[1])

    flag = True

    while flag:
        message = input()

        if message == 'mirror':
            break

        print(find_user(res, message))


f1()
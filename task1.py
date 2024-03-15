def f1():
    with open('history_mirror.txt', encoding='utf8') as f:
        f = f.read()
        errors = [x for x in f.split('\n') if x.split('=')[-1] == 'error']

    with open('mirror_error.txt', mode='a', encoding='utf8') as f:
        for x in errors:
            a = x.split('=')
            f.write(f'У пользователя {a[1]} {a[0]} появилась ошибка'+'\n')

    last = errors[-1].split('=')
    print(f'Ошибка была зафиксирована: {a[0]} у пользователя {a[1]}')


f1()
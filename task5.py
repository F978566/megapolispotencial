from collections import Counter


def f1():
    with open('history_mirror.txt', encoding='utf8') as f:
        f = f.read()
        res = [x.split('=')[-1] for x in f.split('\n')][1:]

    rait = Counter(res)
    rait_dict = dict(Counter(res))
    most_pupolar = rait.most_common()[:5]

    for x in most_pupolar:
        print(f'{x[0]} - {x[1]}')


f1()

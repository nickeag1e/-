def find_food(*food, **param):
    if 'reduce' in param:
        res = [(len(numbers.split()), min(filter(lambda n: n > sum(map(int, numbers.split())) / len(numbers.split()),
                                                 map(int, numbers.split()))) // param['reduce']) for numbers in food]
    else:
        res = [(len(numbers.split()), min(filter(lambda n: n > sum(map(int, numbers.split())) / len(numbers.split()),
                                                 map(int, numbers.split())))) for numbers in food]
    if 'regularize' in param:
        res = sorted(res, reverse=not param['regularize'])
    return res


data = ['1 2 15 14 8 3 6 12 9', '2 3 3 2 1 2 5 2 1 7 2 4', '3 12 8 5 7', '19 8 4 42 13 7 5']
print(*find_food(*data, regularize=False, reduce=2), sep="\n")

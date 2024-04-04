count_fell = 0
count_up = 0


def catch_gnome(string):
    global count_up, count_fell
    if 'gnome' in string.lower():
        count_up += 1
        return f'The gnome stood up {count_up} times.'
    elif 'nils' in string.lower():
        count_fell += 1
        return f'The gnome fell {count_fell} times.'
    else:
        return "It's still a draw."


data = ('Nils shook the net.', 'He floundered helplessly.', 'Gnomes cap had slid down over his nose',
        'His feet were tangled in his wide caftan.')
for item in data:
    print(catch_gnome(item))

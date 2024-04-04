def sweet_dreams(line, n):
    print(', '.join(line.split('. ')[::n]))


line = 'Сны о чём-то лучшем. Мечты о главном. Пусть будет так. Не просыпаться. Вставай!'
slice = 4
sweet_dreams(line, slice)
string = input()
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
alfavit = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
for symbol in set(string):
    if set(symbol) & set(alphabet):
        for i in range(len(alphabet)):
            if symbol == alphabet[i]:
                print((symbol, i + 1))
                break
    if set(symbol) & set(alfavit):
        for i in range(len(alfavit)):
            if symbol == alfavit[i]:
                print((symbol, i + 1))
                break
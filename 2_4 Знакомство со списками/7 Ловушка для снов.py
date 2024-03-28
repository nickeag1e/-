dreams = []
while True:
    dream = input()
    if dream == '':
        break
    else:
        dreams.append(dream)
print(max(dreams[int(input()) - 1:int(input())], key=len))
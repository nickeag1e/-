string1 = input()
string2 = input()
step = 0
if len(string1) != len(string2):
    print('NO')
else:
    while step <= len(string2):
        if string2[step:] + string2[:step] == string1:
            print(step)
            break
        else:
            step += 1
    if step > len(string2):
        print('NO')
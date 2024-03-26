string1 = set(input())
string2 = set(input())
string3 = set(input())
print(''.join(string1 & string2 | string1 & string3 | string2 & string3))
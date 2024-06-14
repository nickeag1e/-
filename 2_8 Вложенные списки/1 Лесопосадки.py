trees = []
while True:
    tree = input()
    if tree:
        trees.append(tree.split(' : '))
    else:
        break
check = int(input())
print('\n'.join('\t'.join(t if int(t) >= check else '0' for t in tree) for tree in trees))

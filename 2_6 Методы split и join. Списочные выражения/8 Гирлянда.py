strings = [list(s) for s in input().split()]
print('_' + '_'.join(s[0] for s in strings) + '_')
print(*[' ' + ' '.join(s[i] if i < len(s) else ' ' for s in strings) + ' '
        for i in range(1, len(max(strings, key=len)))],
      sep='\n')
print(*[' ' + ' '.join(s[i] if i < len(s) else ' ' for s in strings) + ' ' for i in
        range(len(max(strings, key=len)), 0, -1)],
      sep='\n')
print('_' + '_'.join(s[0] for s in strings) + '_')
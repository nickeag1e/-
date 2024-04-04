import sys
print(*[' * '.join(filter(lambda s: 'мачт' in s or 'парус' in s or '-' in s, string.split())) for string in sys.stdin],
      sep='\n')
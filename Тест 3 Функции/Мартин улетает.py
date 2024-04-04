def catch_martin():
    global martin
    martin = ' '.join(sorted(list(filter(lambda s: len(set(s.lower())) >= 4, martin.split())),
                             key=lambda s: len(set(s.lower()))))


martin = 'Wait for me he shouted I am Going with you'
catch_martin()
print(martin)

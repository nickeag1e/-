waves = [input() for i in range(int(input()))]
waves = [(int(wave.split()[-1]), ' '.join(wave.split()[:-1])) for wave in waves]
for i in range(len(waves) - 1):
    if waves[i][0] < waves[i + 1][0]:
        print((i + 1, waves[i][1]))
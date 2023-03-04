'''Impostor'''
import json
def sus():
    '''Don't go lying to me'''
    crew = input()
    data = {}
    while crew != 'Start':
        data.update(json.loads(crew))
        crew = input()

    crew = input()
    kill = []
    while crew != 'End':
        kill.append(crew)
        crew = input()

    imposter = 0
    alive, dead = [], []
    for key, value in data.items():
        if key not in kill:
            alive.append([key, value])
            if value == 'Impostor':
                imposter += 1
        else:
            dead.append([key, value])
    alive.sort(key=lambda x: x[0], reverse=False)
    dead.sort(key=lambda x: x[0])
    print('%s Impostor Remains' % imposter)
    print('***Alive***')
    for i in alive:
        print('%s : %s' % (i[0], i[1]))
    print('***Dead***')
    for i in dead:
        print('%s : %s' % (i[0], i[1]))

sus()

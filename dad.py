def individual (minim,maxum,length):
    return [randint(minim, maxum) for x in range(length)]

grid = {}
forts = {}
for i in range(4, 8):
    forts[i] ={}
    for j in range(6,10):
        forts[i][j] = [8]

for i in range(1, 11):
    grid[i] = {}
    for j in range(1, 11):
        if forts.get(i, None) != None and forts[i].get(j, None) == [8]:
            grid[i][j] = [8]
        else:
            grid[i][j] = []
enemycoords = {}
enemy=0
for x in range(1,4):
    enemy+=1
    x = individual(1,10,4)
    enemycoords[x[0]][x[1]]=x
    grid[x[0]][x[1]]=x
if [5][5] in enemycoords:
    print('key exists')
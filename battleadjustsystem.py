import random


def battle(indiv):
    global grid1,grid2
    global fort_damage

    turns = []

    if type(indiv) == list:
        gridused = grid1
    if type(indiv) == tuple:
        gridused = grid2
    
    while True:     #changed function so that the initial shot isnt random but in the general vicinity of the enemy
        x = random.randint(13,21)
        y = random.randint(1,8)
        shot = gridused[x][y]
        turns.append([x,y])
        if shot [-1] == 'h':
            for i in range(1,10):
                x+=indiv[1]
                y+=indiv[2]
                turns.append([x,y])
            break
        else:
        x = random.randint(1,21)
        y = random.randint(1,21)
        shot = gridused[x][y]
        turns.append([x,y])
    return turns



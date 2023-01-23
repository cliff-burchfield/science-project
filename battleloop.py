def battleloop(indiv, enemy):
    global grid1, grid2
    damage_taken, damage_caused = 0
    indiv_turns = battle(indiv)
    enem_turns = battle(enemy)
    for i, j in zip(range(indiv_turns), range(enem_turns)):
        for x in range (i[2]):
            for y in range (i[2]):
                if grid1[x][y]:
                    grid1[x][y] - 2
        if damage_caused >= 8: #placeholder value. change later
            break
        for x in range (j[2]):
            for y in range (j[2]):
                if grid1[x][y]:
                    grid1[x][y] - 2
        if damage_taken >= 8: #placeholder value. change later
            break
    return damage_caused



def battleloop(indiv, enemy):
    global grid1, grid2
    damage_taken, damage_caused = 0
    indiv_turns = battle(indiv)
    enem_turns = battle(enemy)
    for i, j in zip(range(indiv_turns), range(enem_turns)):
        grid1[i[0]][i[1]]
        if damage_caused >= 8: #placeholder value. change later
            break
        grid2[j[0]][j[1]]
        if damage_taken >= 8: #placeholder value. change later
            break
     return damage_caused
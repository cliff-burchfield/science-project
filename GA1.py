from operator import add
from random import randint
from random import choice
from functools import reduce
import operator
from math import floor

fort_damage = 0
enemy_damage = 0
damage_recieved = 0
grid = {}
mutationchance = 4
ops = {
    1: operator.add,
    0: operator.sub,
}   
#?Creates an individual, a member of the population. Each individaul represents a strategy
def individual (minim,maxum,length):
    return [randint(minim, maxum) for x in range(length)]

#?Creates population
def population(count,length,minim,maxum):
    return [individual(minim,maxum,length) for x in range(count)]

#?Initializes map
def map1(indiv,enemy_list):   
    global grid
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
                grid[i][j] = [8,'f']
            else:
                grid[i][j] = []
    for x in enemy_list:
        grid[x[0]] = {}
        for i in range(1,5):
            grid[x[0]][x[1]] = x + ([6,'e'])
    grid[indiv[0]][indiv[1]] = indiv + ([6,'i'])
    return grid

#Function for attacking

def attack(indiv,grid1):
    global grid
    global fort_damage, enemy_damage, damage_recieved
    newx = randint(1,indiv[2])
    newy = randint(1,indiv[2])
    op_x = randint(0,1)
    op_y = randint(0,1)
  
    newxy = [int(ops[op_x](indiv[0],5)),int(ops[op_y](indiv[1],5))]
    
    if newxy[0] <= 0:
        newxy[0] = indiv[0] + int(round(newy/2))
    if newxy[1] <= 0:
        newxy[1] = indiv[1] + int(round(newx/2))
    if newxy[0] >= 11 or newxy[0]-indiv[3] <= 0 or newxy[0]+indiv[3] > 10:
        newxy[0] = indiv[0] - int(round(newy/2))
    if newxy[1] >= 11 or newxy[1]-indiv[3] <= 0 or newxy[1]+indiv[3] > 10:
        newxy[1] = indiv[1] - int(round(newx/2))
    for i in range(abs(newxy[0]-indiv[3]),abs((newxy[0]+indiv[3])+1)):
        for j in range(abs(newxy[1]-indiv[3]),abs((newxy[1]+indiv[3])+1)):
            if grid1.get(i, None) != None and grid1[i].get(j, None != None) and grid1[i][j]:
                if grid1[i][j][-2] > 0:
                    grid1[i][j][-2] -= 2
                    if grid1[i][j][-1] == 'f':
                        fort_damage += 2
                    elif grid1[i][j][-1] == 'e':
                        enemy_damage += 2
                    elif grid1[i][j][-1] == 'i':
                        damage_recieved += 2
                    else:
                        continue
                if grid1[i][j][-2] <= 0:
                    grid1[i][j] = []
            
#Creates the attack loop
def attack_loop(indiv,enemylist,grid2):
    global grid
    for i in enemylist:
        attack(indiv,grid)
        if not grid[indiv[0]][indiv[1]]:
            break
        attack(i,grid2)
    return [fort_damage, enemy_damage, damage_recieved]

#?Finds the fitness value of an individual
def fitness(indiv):
    global fort_damage, enemy_damage, damage_recieved
    global grid
    enemlist = [individual(1,10,4),individual(1,10,4),individual(1,10,4),individual(1,10,4)]
    grid = map1(indiv,enemlist)
    all_damage = attack_loop(indiv,enemlist,grid)
    fort_damage = all_damage[0]
    enemy_damage = all_damage[1]
    damage_recieved = all_damage[2]
    fitscore = (fort_damage + floor(enemy_damage/1.5)) - floor(damage_recieved*1.5)
    fort_damage = enemy_damage = damage_recieved = 0
    return fitscore

#?Finds the average fitness value of a generation
def pop_grade(pop):  
    summed = reduce(add, (fitness(x) for x in pop))
    return summed/len(pop)


#?Find the best fitness value of a generation
def best_fitness(pop):
    bestfit = 0
    bestchromo = []
    for x in pop:
        fit = fitness(x)
        if fit>bestfit:
            bestfit = fit
            bestchromo = x
    best = "Best Fitness: "+ str(bestfit)+"\n"+"Best Chromosome: "+str(bestchromo)
    return best

#?Creates the roulette wheel for parent selection                  
def wheel(pop):
    result = []
    for p in pop:
        for i in range(0, int(fitness(p))):
            result.append(list(p))
    return result

#?Randomly selects a parent from the wheel
def parent_selection(pop):
    return choice(wheel(pop))

#?Uses the selected parent to create new individuals with crossover
def crossover(pop,length):
    global fort_damage, enemy_damage, damage_recieved
    parent1 = parent_selection(pop)
    parent2 = parent_selection(pop)
    place = randint(1,length)
    chromo1 = parent1[0:place]
    chromo2 = parent2[place:length]
    childchromo = chromo1 + chromo2
    newchromo = list(map(mutation, childchromo)) 
    
    return newchromo

#?Mutates chromosomes
def mutation(gene):  
    if randint(1,100)< mutationchance and gene != 10:
        return gene+1
    elif randint(1,100)< mutationchance and gene == 10:
        return gene-1
    else:
        return gene

dele = open("GAgraphinfo.txt","w")
dele.close()
file = open('GAgraphinfo.txt', 'a')
pop = population(10,4,1,10)
gen = 0
for i in range(1,50):
    gen += 1
    file.write("\n""Gen:  "+ str(gen))
    file.write("\n"+"Gen Average: "+str(pop_grade(pop)))
    file.write("\n"+str(best_fitness(pop))+"\n")
    
    print("\n""Gen:  "+ str(gen))
    print("\n"+"Gen Average: "+str(pop_grade(pop)))
    print("\n"+str(best_fitness(pop)))

    result = []
    for p in pop:
        result += [crossover(pop, 4)]
    pop = result
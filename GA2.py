
from operator import add
import random
from functools import reduce
import operator
from math import floor
import matplotlib.pyplot as plt

grid1 = {}
grid2 = {}
mutationchance = 2.5
ops = {
    1: operator.add,
    0: operator.sub,
}   
#?Creates an individual, a member of the population. Each individaul represents a strategy
def individual(minim,maxum,length):
    genes = [random.randint(minim, maxum) for x in range(length-1)]
    genes.append(random.randint(1,4))
    return genes

#?Creates population
def population(count,length,minim,maxum):
    return [individual(minim,maxum,length) for x in range(count)]

def map():
    grid = {}
    forts = {}
    for i in range(1, 21):
        forts[i] ={}
        for j in range(1,21):
            forts[i][j] = [8]

    for i in range(1, 21):
        grid[i] = {}
        for j in range(1, 21):
            if forts.get(i, None) != None and forts[i].get(j, None) == [8]:
                grid[i][j] = [8, 'f']
            else:
                grid[i][j] = []
    return grid

# #Function for attacking

def battle(indiv):
    global grid1,grid2
    global fort_damage

    turns = []

    if type(indiv) == list:
        gridused = grid1
    elif type(indiv) == tuple:
        gridused = grid2
    else:
        return []
    count = 0
    while True:     #changed function so that the initial shot isnt random but in the general vicinity of the enemy
        count+=1
        x = random.randint(2,19)
        y = random.randint(8,20)
        shot = gridused[x][y]
        turns.append([x,y])
        if shot:
            if shot [1] == 'f':
                for i in range(1,10):
                    x+=indiv[1]
                    y+=indiv[2]
                    turns.append([x,y])
                break
    return turns

            
# #Creates the attack loop
def battleloop(indiv, enemy):
    global grid1, grid2
    damage_taken = 0
    damage_caused = 0
   
    indiv_turns = battle(indiv)
    enem_turns = battle(enemy)
    for i, j in zip((indiv_turns), (enem_turns)):
        for x in range (i[0]-indiv[2],i[0]+1):
            for y in range (i[0]-indiv[2],i[1]+1):
                if x in grid1:
                    if y in grid1[x]:
                        if grid1[x][y]:
                          grid1[x][y][0] - 2
        if damage_caused >= 8: #placeholder value. change later
            break
        for x in range (j[0]):
            for y in range (j[1]):
                if x in grid2:
                    if y in grid1[x]:
                        if grid1[x][y]:
                          grid1[x][y][0] - 2
        if damage_taken >= 8: #placeholder value. change later
            break
    return damage_caused

# #?Finds the fitness value of an individual
def fitness(indiv):
    global grid1, grid2
    enem = tuple(individual(1,10,3))
    grid1 = map()
    grid2 = map()
    fitscore = battleloop(indiv,enem)
    return fitscore



#?Find the best fitness value of a generation
def display_fitness(pop):
    bestfit = 0
    bestchromo = []
    for x in pop:
       
        fit = fitness(x)
        
        if fit>bestfit:
            bestfit = fit
            bestchromo = x
    best = "Best Fitness: "+ str(bestfit)+"\n"+"Best Chromosome: "+str(bestchromo)
    return best

def fitnesses(pop):
    bestfit = 0
    bestchromo = []
    for x in pop:
        fit = fitness(x)
        if fit>bestfit:
            bestfit = fit
            bestchromo = x
    return [[bestfit],[bestchromo]]

#?Creates the roulette wheel for parent selection                  
def wheel(pop):
    result = []
    print(pop)
    if type(pop) != list and type(pop) != tuple:
        quit()
    for p in pop:
        for i in range(0, int(fitness(p))):
            result.append(list(p))
    return result

#?Randomly selects a parent from the wheel
def parent_selection(pop):
    
    return random.choice(wheel(pop))

#?Uses the selected parent to create new individuals with crossover
def crossover(pop, length):
    global fort_damage, enemy_damage, damage_recieved
    parent1 = parent_selection(pop)
    parent2 = parent_selection(pop)
    place = random.randint(1,length)
    chromo1 = parent1[0:place]
    chromo2 = parent2[place:length]
    childchromo = chromo1 + chromo2
    newchromo = list(map(mutation, childchromo)) 
    
    return newchromo

#?Mutates chromosomes
def mutation(gene):  
    if random.randint(1,100)< mutationchance and gene != 1:
        return gene-1
    elif random.randint(1,100)< mutationchance and gene == 1:
        return gene+1
    else:
        return gene

dele = open("GAgraphinfo.txt","w")
dele.close()
file = open('GAgraphinfo.txt', 'a')
pop = population(15,3,-10,11)

y = []
y2 = []
#average = []
gen = 0
for i in range(1,500+1):
    gen += 1
    file.write("Gen:  "+ str(gen)+"\n")
    file.write(str(display_fitness(pop))+"\n")
    
    y.append(fitnesses(pop)[0])
    
    print("Gen:  "+ str(gen))
    print(str(display_fitness(pop))+"\n")

   # average.append(indivdamage/diviindiv)
    
    result = []
    for x in range(1, len(pop) + 1):
        result += [crossover(pop, 4)]
    pop = result

x = range(1,gen+1) 
plt.figure('Best Fitness Over Each Generation')
plt.plot(x, y, label='Best Fitness')
plt.title('Best Fitness Over Each Generation')
plt.xlabel('Generation')
plt.ylabel('Fitness Value')
plt.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')

plt.show()
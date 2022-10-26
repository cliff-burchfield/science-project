from operator import add
from random import randint
from random import choice
from functools import reduce
import operator

fort_damage = 0
enemy_damage = 0
damage_recieved = 0
grid = {}
mutationchance = 3
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
def map(indiv):   
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
                grid[i][j] = ['f',8]
            else:
                grid[i][j] = []
    for x in range(1,4):
        x = individual(1,10,4)
        grid[x[0]] = {}
        for i in range(1,4):
            grid[x[0]][x[1]] = x.extend([6,'e'])
    grid[indiv[0]][indiv[1]] = indiv.extend([6,'i'])

def attack(indiv,grid):
    newx = randint(1,indiv[2])
    newy = randint(1,indiv[2])
    op_x = randint(0,1)
    op_y = randint(0,1)

    newxy = [ops[op_x](indiv[0],5),ops[op_y](indiv[1],5)]
    grid[newxy[0]][newxy[1]]
    if newxy[0] <= 0:
        newxy[0] = indiv[0] + round(newx/2)
    if newxy[1] <= 0:
        newxy[1] = indiv[1] + round(newx/2)
    if newxy[0] >= 11:
        newxy[0] = indiv[0] - round(newx/2)
    if newxy[1] >= 11:
        newxy[1] = indiv[1] - round(newx/2)
    
    for i in (newxy[0]-newxy[4],newxy[0]+newxy[4]+1):
        for j in (newxy[1]-newxy[4],newxy[1]+newxy[4]+1):
            if indiv =< 0:
                grid[i][j] = []
                if indiv[-1] == 'f':
                    fort_damage += 2
                elif indiv[-1] == 'e':
                    fort_damage += 2
                elif indiv[-1] == 'i':
                    damage_recieved += 2
            f grid[i][j] != False:
                indiv[-2]-2

            

#?Finds the fitness value of an individual
def fitness(individual):
    indiv = individual
    grid = map(indiv)
    fort_damage = ''
    enemy_damage = ''
    damage_recieved = ''
    fitscore = fort_damage + round(enemy_damage/1.5) - round(damage_received*1.5)
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
        for i in range(0, fitness(p)):
            result.append(list(p))
    return result

#?Randomly selects a parent from the wheel
def parent_selection(pop):
    return choice(wheel(pop))

#?Uses the selected parent to create new individuals with crossover
def crossover(pop,length):
    parent1 = parent_selection(pop)
    parent2 = parent_selection(pop)
    place = randint(1,length)
    chromo1 = parent1[0:place]
    chromo2 = parent2[place:length]
    childchromo = chromo1 + chromo2
    newchromo = list(map(mutation, childchromo)) 
    return newchromo

#?Mutates chromosomes
def mutation(gene):     #may be changed
    if randint(1,100)< mutationchance :
        return gene+1
    else:
        return gene

endnum = 0
endcheck = ''
dele = open("GAallinfo.txt","w")
dele.close()
file = open('GAallinfo.txt', 'a')
pop = population(4,1,0,9)
gen = 0
# while endnum != 1:   ##Placeholder true statement##
#     gen += 1
#     file.write("\n""Gen:  "+ str(gen))
#     file.write("\n"+"Gen Average: "+str(pop_grade(pop)))
#     file.write("\n"+str(best_fitness(pop)))
#     print("\n""Gen:  "+ str(gen))
#     print("\n"+"Gen Average: "+str(pop_grade(pop)))
#     print("\n"+str(best_fitness(pop)))
#     result = []
#     for p in pop:
#         result += [crossover(pop, 4)]
#     if best_fitness(pop) == endcheck:
#         endnum += 1
#     elif best_fitness(pop) != endcheck:
#         endnum = 0
#         endcheck = pop_grade(pop)
#     pop = result




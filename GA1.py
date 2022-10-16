from operator import add
from random import randint
from random import choice
from functools import reduce

mutationchance = .04

#?Creates an individual, a member of the population. Each individaul represents a strategy
# Input: Int, int, int
# Output: List of ints
def individual (minim,maxum,length):
    return [randint(minim, maxum) for x in range(length)]

#?Creates population
# Input: Int, int, int, int
# Output: List of lists of ints
def population(count,length,minim,maxum):

    #count = number of individuals in pop
    #length = number of values per individual
    #minim = the min possible value in an individual's chromosomes
    #maxum = max possible value in an individual's chromosomes

    return [individual(minim,maxum,length) for x in range(count)]

#?Finds the fitness value of an individual
# Input: List of int
# Output: Int
def fitness(individual):                    #! This fitness function is only an example and a placeholder. 
                                                    #!it will eventually be modified for the actual GA. For example, 
    #individual = an indiviual of the population    #!the solution is predetermined in the target, but in the real GA there will be no target
    strindi = map(str,individual)
    intindi = int("".join(strindi))
    fitscore = 10 - intindi
    return fitscore

#?Finds the average fitness value of a generation
# Input: List of lists of ints
# Output: Int
def pop_grade(pop):  
    summed = reduce(add, (fitness(x) for x in pop))
    return summed/len(pop)


#?Find the best fitness value of a generation
# Input: List of lists of ints
# Output: Int 
def best_fitness(pop):
    bestfit = 0
    for x in pop:
        if fitness(x)>bestfit:
            bestfit = x
    return bestfit

#?Creates the roulette wheel for parent selection   
# Input: List of lists of int
# Output: List of lists of int               
def wheel(pop):
    result = []
    for p in pop:
        for i in range(0, fitness(p)):
            result.append(p.copy())
    return result

#?Randomly selects a parent from the wheel
# Input: List of lists of ints
# Output: List of ints
def parent_selection(pop):
    return choice(wheel(pop))

#?Uses the selected parent to create new individuals with crossover
# Input: List of lists of ints, int
# Output: List of ints
def crossover(pop,length):
    parent1 = parent_selection(pop)
    parent2 = parent_selection(pop)
    place = randint(1,length)
    chromo1 = parent1[0:place]
    chromo2 = parent2[place:length]
    childchromo = chromo1 + chromo2
    newchromo = list(map(mutation, childchromo)) 
    return newchromo

    #for x in newgene:
    #    if random.randint(1,100)<mutationchance:
    #        x = mutation(x)

#?Mutates chromosomes
# Input: Int
# Output: Int
def mutation(gene):     #may be changed
    if randint(1,100)< mutationchance :
        return gene+.01
    else:
        return gene

pop = population(50,1,0,9)
while True:   ##Placeholder true statement##
    with open("GAallinfo.txt","w") as file:
        file.write(str(pop_grade(pop)))
    result = []
    for p in pop:
        result += crossover(pop, 1)
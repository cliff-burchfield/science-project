from operator import add
from random import randint
from functools import reduce

mutationchice = .04

#?Creates an individual, a member of the population. Each individaul represents a strategy
def individual (minim,maxum,length):
    return [randint(minim, maxum) for x in range(length)]

#?Creates population
def population(count,length,minim,maxum):

    #count = number of individuals in pop
    #length = number of values per individual
    #minim = the min possible value in an individual's chromosomes
    #maxum = max possible value in an individual's chromosomes

    return [individual(minim,maxum,length) for x in range(count)]

#?Finds the fitness value of an individual
def fitness(individual, target):                    #! This fitness function is only an example and a placeholder. 
                                                    #!it will eventually be modified for the actual GA. For example, 
    #individual = an indiviual of the population    #!the solution is predetermined in the target, but in the real GA there will be no target
    #target = fitness value we are aiming for.

    fitscore = 0
    for (x,y) in zip(individual,target):    
        if x==int(y):
            fitscore+=1         
    return int(fitscore)*2

#?Finds the average fitness value of a generation
def pop_grade(pop,target):
    summed = reduce(add, (fitness(x,target) for x in pop))
    return summed/len(pop)

#x = population(3,5,0,10)
#print(pop_grade(x, "50001"))

#?Find the total fitness value of a generation
def total_fitness(pop,target):
    return reduce(add, (fitness(x,target) for x in pop))

#?Selects parents for the new individuals                          
def parent_selection(pop,target):
    wheel = list(map(lambda x:list(x*fitness(x,target)), pop))

#?Uses the selected parent to create new individuals with crossover
def crossover(length,parent1,parent2):
    place = random.randint(1,length)
    genep1 = parent1[0:place]
    genep2 = parent2[place:length]
    childgene = genep1 + genep2
    newgene = list(map(mutation, newgene)) 
    return newgene

    #for x in newgene:
    #    if random.randint(1,100)<mutationchance:
    #        x = mutation(x)

#?Mutates chromosomes
def mutation(chromosome):     #may be changed
    if random.randint(1,100)<mutationchance:
        return chromosome+.01
    else:
        return chromosome
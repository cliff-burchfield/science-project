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
def fitness(individual):                    #! This fitness function is only an example and a placeholder. 
                                                    #!it will eventually be modified for the actual GA. For example, 
    #individual = an indiviual of the population    #!the solution is predetermined in the target, but in the real GA there will be no target
    intindi = int(individual)
    fitscore = intindi - 100
    return fitscore

#?Finds the average fitness value of a generation
def pop_grade(pop):
    summed = reduce(add, (fitness(x) for x in pop))
    return summed/len(pop)

#x = population(3,5,0,10)
#print(pop_grade(x, "50001"))

#?Find the total fitness value of a generation
def total_fitness(pop):
    return reduce(add, (fitness(x) for x in pop))

#?Creates the roulette wheel for parent selection                          
def wheel(pop):
    result = []
    for p in pop:
        for i in range(0, fitness(p)):
            result.append(p.copy())
    return result

def parent_selection(pop):
    return random.choice(wheel(pop))

#?Uses the selected parent to create new individuals with crossover
def crossover(pop,length):
    parent1 = parent_selection(pop)
    parent2 = parent_selection(pop)
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

pop = population(50,1,0,9)
while True:   ##Placeholder true statement##
    with open("GAallinfo.txt","w") as file:
        file.write(pop_grade(pop))
    pop = reduce(crossover(pop,1) for x in pop)
   
    # for i in range(0,pop):
    #     crossover(1,parent1,parent2)
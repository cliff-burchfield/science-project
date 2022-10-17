import random
from functools import reduce
from operator import add

def function1(a,b):
    c=(a*a)+(b*b)
    return c
function1(3,4)
function1=6
#print(function1)

#print(random.randint(0,1))

##ex=[1,2,3,4]
##print(ex[2-1:4])

length=5
parent1=[1,2,4,6,3]
parent2=[2,3,1,4,5]
#place = random.randint(1,length)
#genep1 = parent1[0:place]
#genep2 = parent2[place:length]
mutationchance = 90
#print(place)
#print(genep1)
#print(genep2)
#?Mutates chromosomes
def mutation(chromosome):     #may be changed
    if random.randint(1,100)<mutationchance:
        return chromosome+.01
    else:
        return chromosome

place = random.randint(1,length)
genep1 = parent1[0:place]
genep2 = parent2[place:length]
childgene = genep1 + genep2
newgene = list(map(mutation, childgene))

    #for x in newgene:
    #    if random.randint(1,100)<mutationchance:
    #        x = mutation(x)

#print(genep1)
#print(genep2)
#print(childgene)
#print(newgene)

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

# #x = population(3,5,0,10)
# #print(pop_grade(x, "50001"))

#?Find the total fitness value of a generation
def total_fitness(pop,target):
    total = reduce(add, (fitness(x,target) for x in pop))
    return total

pop = [[1,2,3,4,5],[7,2,5,9,2],[6,3,3,4,2]]
target = '12345'

# print(pop_grade(pop,target))
# print(total_fitness(pop,target))

# print(random.choice([[1,2,3,4,5],[4,5,6],[7,8,9]]))

#list(fitness(x,target) for x in pop)

# wheel = []         
# for x in pop:
#     wheel+(x*fitness(x,target))
#def wheel(pop, x):
#    result = []
#    for i in range(0, x):
#     result += pop.copy()
#    return result;

# def wheel(pop):
#     result = []
#     for p in pop:
#         for i in range(0, fitness(p, target)):
#             result.append(p.copy())
#     return result
# # print(pop)
# # print(target)

# # print(wheel)

# print(wheel(pop))

count=0
for i in range(0,10):
    count+=1
print (count)
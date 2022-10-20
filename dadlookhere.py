import random
individual = [1,2,3,4]
import operator

newx = random.randint(1,individual[2])
newy = random.randint(1,individual[2])
enemylist = [[1,2,3,4]]
grid = {}
forts = {}
for i in range(4, 8):
    forts[i] ={}
    for j in range(6,10):
        forts[i][j] = [8]

for i in range(1, 11):
    grid[i] = {}
    for j in range(1, 11):
        grid[i][j] = []
for x in enemylist:
    grid[x[0]] = {}
    for i in range(1,4):
        grid[x[0]][x[1]] = x.append(6)
grid[individual[0]][individual[1]] = individual.append(6)

ops = {
    1: operator.add,
    0: operator.sub,
}   
op_x = random.randint(0,1)
op_y = random.randint(0,1)

newxy = grid[ops[op_x](individual[0],newx)][ops[op_y](individual[1],newy)]

if newxy[0] <= 0:
    newxy[0] = individual[0] + round(newx/2)
if newxy[1] <= 0:
    newxy[1] = individual[1] + round(newx/2)
if newxy[0] >= 11:
    newxy[0] = individual[0] - round(newx/2)
if newxy[1] >= 11:
    newxy[1] = individual[1] - round(newx/2)
## Make it so if any of the values are less than
## 1 than add half (rounded) of the value instead of subtract full
## and if it becomes more than 10 subtract half of that (rounded)
## instead
## Need dad's help
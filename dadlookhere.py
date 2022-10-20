addsub_x = random.randint(0,1)
addsub_y = random.randint(0,1)

import operator
ops = {
    1: operator.add,
    0: operator.sub,
}   
op_char = random.randint(0,1)

if grid[ops[op_x](individual[0],newx)][ops[op_y](individual[1],newy)] <= 0 or grid[ops[op_x](individual[0],newx)][ops[op_y](individual[1],newy)] <= 0:
## Make it so if any of the values are less than
## 1 than add half (rounded) of the value instead of subtract full
## and if it becomes more than 10 subtract half of that (rounded)
## instead
## Need dad's help
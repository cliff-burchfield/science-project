grid1 = {}
grid2 = {}

def map():
    grid = {}
    forts = {}
    for i in range(4, 18):
        forts[i] ={}
        for j in range(10,19):
            forts[i][j] = [8]

    for i in range(1, 21):
        grid[i] = {}
        for j in range(1, 21):
            if forts.get(i, None) != None and forts[i].get(j, None) == [8]:
                grid[i][j] = [8]
            else:
                grid[i][j] = []
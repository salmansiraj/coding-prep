def rottenOranges(self, grid: List[List[int]]) -> int:

    if not grid:
        return -1

    fresh = set()
    rotten = set()

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                fresh.add((i, j))
            if grid[i][j] == 2:
                rotten.add((i, j))

    if len(fresh) == 0:
        return 0

    minutes = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while len(fresh) > 0:
        infected = set()
        for i, j in rotten:
            for x, y in directions:
                nextI = i + x
                nextJ = j + y
                if (nextI, nextJ) in fresh:
                    fresh.remove((nextI, nextJ))
                    infected.add((nextI, nextJ))

        if len(infected) == 0:
            return -1

        rotten = infected
        minutes += 1

    return minutes

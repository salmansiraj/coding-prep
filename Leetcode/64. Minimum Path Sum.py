def minPathSum(self, grid: List[List[int]]) -> int:
    maxRow = len(grid)
    maxCol = len(grid[0])

    dpGrid = [[0] * maxCol for i in range(maxRow)]
    dpGrid[0][0] = grid[0][0]

    for i in range(1, maxRow):
        dpGrid[i][0] = dpGrid[i - 1][0] + grid[i][0]

    for j in range(1, maxCol):
        dpGrid[0][j] = dpGrid[0][j - 1] + grid[0][j]

    for i in range(1, maxRow):
        for j in range(1, maxCol):
            dpGrid[i][j] = grid[i][j] + min(dpGrid[i][j - 1], dpGrid[i - 1][j])

    return dpGrid[-1][-1]

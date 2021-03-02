'''
    O(n^2) for dfs search
'''


def exist(self, board: List[List[str]], word: str) -> bool:
    visited = [[False] * len(board[i]) for i in range(len(board))]

    def search(board, row, col, word):
        if len(word) == 0:
            return True

        visited[row][col] = True
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for x, y in directions:
            if (row + x < len(board) and row + x >= 0 and col + y < len(board[row]) and col + y >= 0) and board[row + x][col + y] == word[0] and visited[row + x][col + y] != True:
                if search(board, row + x, col + y, word[1:]):
                    return True

        visited[row][col] = False
        return False

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == word[0]:
                if search(board, i, j, word[1:]):
                    return True

    return False

from typing import List

def islands(matrix: List[List[str]]) -> int:
    rows = len(matrix)
    cols = len(matrix[0])

    result = 0

    for r in range(rows):
        for c in range(cols):

            if matrix[r][c] == "1":
                result += 1

                dfs(matrix, r, c) 

    return result

def dfs(matrix, r, c):

    if (c < 0 or r < 0 or c > len(matrix[0]) or r > len(matrix)): return
    if matrix[r][c] == 0: return

    matrix[r][c] = 0

    dfs(matrix, r, c+1)
    dfs(matrix, r, c-1)
    dfs(matrix, r+1, c)
    dfs(matrix, r-1, c)
    
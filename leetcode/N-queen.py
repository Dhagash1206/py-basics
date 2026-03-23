def isSafe(mat, row, col):
    n = len(mat)

    for i in range(row):
        if mat[i][col]:
            return 0

    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if mat[i][j]:
            return 0
        i -= 1
        j -= 1

    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if mat[i][j]:
            return 0
        i -= 1
        j += 1

    return 1

def placeQueens(row, mat, result):
    n = len(mat)

    if row == n:
        ans = []
        for i in range(n):
            for j in range(n):
                if mat[i][j]:
                    ans.append(j + 1)
        result.append(ans)
        return

    for i in range(n):
        if isSafe(mat, row, i):
            mat[row][i] = 1
            placeQueens(row + 1, mat, result)
            mat[row][i] = 0

def nQueen(n):
    mat = [[0] * n for _ in range(n)]
    result = []
    placeQueens(0, mat, result)
    return result

if __name__ == "__main__":
    n = 4
    result = nQueen(n)
    for ans in result:
        print(" ".join(map(str, ans)))

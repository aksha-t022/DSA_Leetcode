class Solution:
    def shiftGrid(self, grid, k):
        m = len(grid)
        n = len(grid[0])

        arr = []

        for i in range(m):
            for j in range(n):
                arr.append(grid[i][j])

        k = k % len(arr)
        arr = arr[-k:] + arr[:-k]

        result = []
        x = 0

        for i in range(m):
            row = []
            for j in range(n):
                row.append(arr[x])
                x += 1
            result.append(row)

        return result
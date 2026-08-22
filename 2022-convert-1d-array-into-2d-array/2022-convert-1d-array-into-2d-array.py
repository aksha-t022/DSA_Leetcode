class Solution:
    def construct2DArray(self, original, m, n):
        if len(original) != m * n:
            return []

        result = []
        k = 0

        for i in range(m):
            row = []
            for j in range(n):
                row.append(original[k])
                k += 1
            result.append(row)

        return result
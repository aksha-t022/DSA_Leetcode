class Solution:
    def climbStairs(self, n: int) -> int:
        d = {}
        def helpFunction(n):
            if n<=2:
                return n
            if n in d:
                return d[n]
            temp = helpFunction(n-1) + helpFunction(n-2)
            d[n] = temp
            return temp

        return helpFunction(n)
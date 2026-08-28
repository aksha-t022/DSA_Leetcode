class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        path = set()
        safe = set()

        def dfs(node):
            if node in path:
                return False

            if node in safe:
                return True

            path.add(node)

            for i in graph[node]:
                if not dfs(i):
                    return False

            path.remove(node)
            safe.add(node)

            return True

        op = []

        for i in range(len(graph)):
            if dfs(i):
                op.append(i)

        return op
class Solution:
    def canVisitAllRooms(self, rooms):
        n = len(rooms)
        vis = [False] * n
        q = []

        for x in rooms[0]:
            q.append(x)
            vis[x] = True

        vis[0] = True
        i = 0

        while i < len(q):
            room = q[i]
            i += 1

            for x in rooms[room]:
                if not vis[x]:
                    q.append(x)
                    vis[x] = True

        return all(vis)
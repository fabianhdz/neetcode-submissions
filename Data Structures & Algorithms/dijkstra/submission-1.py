from collections import deque
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        dq = deque()
        cost = [float('inf')] * n
        cost[src] = 0

        dq.append(src)

        adj = {}
        for i in range(n):
            adj[i] = []

        for s, v, w in edges:
            adj[s].append([v, w])


        while dq:

            curr = dq.popleft()

            for neighbor, weight in adj[curr]:
                    if cost[neighbor] > cost[curr] + weight:
                        cost[neighbor] = cost[curr] + weight
                        dq.append(neighbor)
        
        for i in range(n):
            if cost[i] == float('inf'):
                cost[i] = -1
                            

        return { idx: c for idx, c in enumerate(cost)}

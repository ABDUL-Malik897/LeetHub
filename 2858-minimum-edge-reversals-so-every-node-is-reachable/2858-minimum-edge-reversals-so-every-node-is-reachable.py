class Solution(object):

    def minEdgeReversals(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        graph = [[] for _ in range(n)]

        # u -> v is original direction: cost 0
        # v -> u is reverse direction: cost 1
        for u, v in edges:
            graph[u].append((v, 0))
            graph[v].append((u, 1))

        # First pass: calculate answer for node 0
        parent = [-1] * n
        cost = [0] * n
        order = [0]

        for u in order:
            for v, c in graph[u]:
                if v == parent[u]:
                    continue

                parent[v] = u
                cost[v] = c
                order.append(v)

        ans = [0] * n

        # Number of reversals needed when starting from node 0
        for i in range(1, n):
            ans[0] += cost[i]

        # Second pass: reroot the answer
        for u in order:
            for v, c in graph[u]:
                if v == parent[u]:
                    continue

                # Move root from u to v
                ans[v] = ans[u] + 1 - 2 * c

        return ans
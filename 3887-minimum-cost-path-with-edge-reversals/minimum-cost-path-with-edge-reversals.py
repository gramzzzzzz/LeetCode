class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        rg = defaultdict(list)
        for i, j, w, in edges:
            g[i].append([j, w])
            g[j].append([i, 2*w])
        h = [(0, 0)]
        wts = [float('inf')] * n
        wts[0] = 0
        while h:
            cost, cur = heapq.heappop(h)
            if cur == n-1:
                return cost
            for adj, w in g[cur]:
                if cost+w < wts[adj]:
                    wts[adj] = cost+w
                    heapq.heappush(h, (wts[adj], adj))
            for adj, w in rg[cur]:
                if cost+w < wts[adj]:
                    wts[adj] = cost+w
                    heapq.heappush(h, (wts[adj], adj))
        return -1
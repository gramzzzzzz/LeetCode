class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        @cache
        def helper(i, j):
            ans = 1
            for dx, dy in d:
                r = i+dx
                c = j+dy
                if 0 <= r < m and 0 <= c < n and grid[r][c] > grid[i][j]:
                    ans += helper(r, c)
            return ans % 1000000007

        ans = 0
        for i in range(m):
            for j in range(n):
                ans += helper(i, j) 
        return ans % 1000000007
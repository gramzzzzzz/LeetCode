class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        @cache
        def dfs(i, j, d):
            if i == m-1 and j == n-1:
                return 1
            if not (0 <= i < m) or not (0 <= j < n):
                return 0
            ans = 0
            if grid[i][j] == 0:
                ans += dfs(i+1, j, 1)
                ans += dfs(i, j+1, 0)
            else:
                if d == 0:
                    ans += dfs(i+1, j, 1)
                else:
                    ans += dfs(i, j+1, 0)
            return ans

        return dfs(0, 0, 0) % 1000000007
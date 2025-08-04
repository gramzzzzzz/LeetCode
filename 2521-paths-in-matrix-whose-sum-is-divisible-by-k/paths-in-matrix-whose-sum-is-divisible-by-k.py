class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0

        mem = {}

        def helper(i, j, s):
            if i == m-1 and j == n-1:
                return int((s+grid[i][j])%k == 0)
            if i >= m or j >= n:
                return 0
            if (i, j, s) in mem:
                return mem[(i, j, s)]
            # ans = 0
            # if j+1 < n:
            #     ans += helper(i, j+1, (s+grid[i][j+1])%k)
            # if i+1 < m:
            #     ans += helper(i+1, j, (s+grid[i+1][j])%k)
            ans = (helper(i, j+1, (s+grid[i][j])%k) + helper(i+1, j, (s+grid[i][j])%k)) % 1000000007
            mem[(i, j, s)] = ans
            return ans
        
        return helper(0, 0, 0) % 1000000007

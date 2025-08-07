class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)

        child1 = 0
        for i in range(n):
            child1 += fruits[i][i]
            fruits[i][i] = 0

        dx = [[1, 1, 1], [-1, 0, 1]]
        dy = [[-1, 0, 1], [1, 1, 1]]
        
        @cache
        def helper(i, j, k):
            if i == n-1 and j == n-1:
                return fruits[i][j]
            if i < 0 or i >= n or j < 0 or j >= n or (k==0 and i >= j) or (k==1 and i <= j):
                return float('-inf')
            ans = float('-inf')
            for x in range(3):
                ans = max(ans, fruits[i][j]+helper(i+dx[k][x], j+dy[k][x], k))
            return ans

        child2 = helper(0, n-1, 0)
        child3 = helper(n-1, 0, 1)
        return child1+child2+child3

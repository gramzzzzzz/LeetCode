class Solution:
    def minDays(self, n: int) -> int:
        @cache
        def helper(n):
            if n == 1:
                return 1
            if n == 0:
                return 0
            # ans = float('inf')
            # ans = min(ans, (n%2)+1+helper((n-(n%2))//2))
            # ans = min(ans, (n%3)+1+helper((n-(n%3))//3))
            return min((n%2)+1+helper((n-(n%2))//2), (n%3)+1+helper((n-(n%3))//3))
            return ans
        
        return helper(n)
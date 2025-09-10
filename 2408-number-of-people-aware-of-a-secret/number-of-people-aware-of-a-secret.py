class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        
        @cache
        def helper(curn):
            if curn > n:
                return 0
            if curn == n:
                return 2
            if curn+delay > n:
                return 1
            ans = 0
            for i in range(curn+delay, curn+forget):
                ans += helper(i)
            return ans%1000000007
        
        return helper(1)
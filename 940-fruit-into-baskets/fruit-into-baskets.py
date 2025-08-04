class Solution:
    def totalFruit(self, nums: List[int]) -> int:
        n = len(nums)
        d = defaultdict(int)
        els = 0
        l, r = 0, 0
        ans = 0
        while r < n:
            if d[nums[r]] == 0:
                els += 1
            d[nums[r]] += 1
            while els > 2:
                d[nums[l]] -= 1
                if d[nums[l]] == 0:
                    els -= 1
                l += 1
            ans = max(ans, r-l+1)
            r += 1
        return ans
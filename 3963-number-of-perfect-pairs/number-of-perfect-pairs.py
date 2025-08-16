class Solution:
    def perfectPairs(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            nums[i] = abs(nums[i])
        nums.sort()
        # tmp = bisect_left(nums, 0)
        ans = 0
        for i in range(n):
            ind = bisect_left(nums, nums[i]/2, 0, i)
            # if ind < i:
                # ind = max(ind, tmp)
            ans += (i-ind)
        return ans
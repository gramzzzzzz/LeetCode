class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        ans = float('inf')
        for i in range(n-1, -1, -1):
            ans = min(ans, n-i-1+bisect_left(nums, nums[i]/k))
        return ans
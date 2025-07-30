class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # n = len(nums)
        isFlipped = False
        ans = 0
        for i in nums:
            # if (nums[i] == 0 and not isFlipped) or (nums[i] == 1 and isFlipped):
            if not i^isFlipped:
                ans += 1
                isFlipped = not isFlipped
        return ans 
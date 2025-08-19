class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        cnt = 0
        for i in nums:
            if i == 0:
                cnt += 1
            else:
                cnt = 0
            ans += cnt
        return ans

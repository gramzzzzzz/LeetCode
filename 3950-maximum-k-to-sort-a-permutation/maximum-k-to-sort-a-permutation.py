class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        arr = sorted(nums)
        set = [0] * 32
        cnt = 0
        for i in range(n):
            if arr[i] != nums[i]:
                tmp = nums[i]
                ind = 31
                cnt += 1
                while tmp != 0:
                    if tmp&1:
                        set[ind] += 1
                    tmp >>= 1
                    ind -= 1
        ans = 0
        mul = 1
        if cnt == 0:
            return 0
        for i in range(31, -1, -1):
            if set[i] == cnt:
                ans += mul
            mul *= 2
        return ans
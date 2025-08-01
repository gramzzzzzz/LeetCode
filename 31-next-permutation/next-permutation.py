class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        ind = -1
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                ind = i
                break
        if ind == -1:
            for i in range(n//2):
                nums[i], nums[n-i-1] = nums[n-i-1], nums[i]
            return
        tmp = nums[-1]
        swap_ind = -1
        for i in range(n-1, ind, -1):
            if nums[i] > nums[ind]:
                swap_ind = i
                break
        # print(ind, swap_ind)
        nums[ind], nums[swap_ind] = nums[swap_ind], nums[ind]
        l = ind+(n-ind-1)//2+1
        for i in range(ind+1, l):
            nums[i], nums[ind+n-i] = nums[ind+n-i], nums[i]
        return
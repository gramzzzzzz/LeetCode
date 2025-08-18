class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        q = len(queries)
        for i, j, k, v in queries:
            for x in range(i, j+1, k):
                nums[x] = (nums[x]*v)%(1000000007)
        xor = nums[0]
        for i in range(1, n):
            xor ^= nums[i]
        return xor
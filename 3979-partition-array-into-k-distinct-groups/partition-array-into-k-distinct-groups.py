class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n%k !=  0:
            return False
        g = n//k
        d = Counter(nums)
        for i in d:
            if d[i] > g:
                return False
        return True
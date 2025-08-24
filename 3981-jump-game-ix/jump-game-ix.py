class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = []
        for i in range(n):
            arr.append((nums[i], i))
        arr.sort()
        pref = [0] * n
        pref[0] = arr[0][1]
        for i in range(1, n):
            pref[i] = max(pref[i-1], arr[i][1])
        prefm = [0] * n
        prefm[0] = nums[0]
        for i in range(1, n):
            prefm[i] = max(prefm[i-1], nums[i])
        # print(arr)
        # print(pref)
        # print(prefm)
        ans = [0] * n
        for i in range(n-1, -1, -1):
            m = prefm[i]
            ind = bisect_right(arr, (m-1, float('inf')))
            # print(nums[i], m, ind)
            # ind = min(ind, n-1)
            if ind > 0:
                target_ind = pref[ind-1]
                ans[i] = max(prefm[target_ind], ans[target_ind], nums[i])
            else:
                ans[i] = nums[i]
        return ans
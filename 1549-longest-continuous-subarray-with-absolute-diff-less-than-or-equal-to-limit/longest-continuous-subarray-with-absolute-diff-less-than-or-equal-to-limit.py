class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        l, r = 0, 0
        ans = 1
        h = []
        hm = []
        s = set()
        while r < n:
            heapq.heappush(h, (nums[r], r))
            heapq.heappush(hm, (-nums[r], r))
            while h and hm and abs(h[0][0]+hm[0][0]) > limit:
                s.add(l)
                l += 1
                while h and h[0][1] in s:
                    heapq.heappop(h)
                while hm and hm[0][1] in s:
                    heapq.heappop(hm)
            ans = max(ans, r-l+1)
            r += 1
        return ans
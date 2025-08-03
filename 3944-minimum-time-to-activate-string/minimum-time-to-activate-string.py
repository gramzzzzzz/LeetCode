class Solution:
    def minTime(self, s: str, order: List[int], k: int) -> int:
        n = len(s)

        def check(ind):
            cnt = n*(n+1)//2
            arr = sorted(order[:ind+1])
            pr = -1
            for i in arr:
                tmp = i-1-pr
                cnt -= tmp*(tmp+1)//2
                pr = i
            cnt -= (n-1-pr)*(n-pr)//2
            return cnt >= k

        l = 0
        r = n-1
        while l <= r:
            mid = (l+r)//2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l if l < n else -1
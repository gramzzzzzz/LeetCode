class Solution:
    def maxTotal(self, values: List[int], limit: List[int]) -> int:
        n = len(values)
        arr = []
        for i in range(n):
            arr.append((limit[i], values[i]))
        arr.sort(key=lambda x: (x[0], -x[1]))
        cur = 0
        ans = 0
        l = 0
        for k in range(n):
            i = arr[k][0]
            j = arr[k][1]
            if cur < i and l <= k:
                ans += j
                cur += 1
                if l < n:
                    ind = bisect_right(arr, (cur,float('inf')), l, n)
                    if ind > l:
                        cur = max(cur-(ind-l), 0)
                        l = ind
        return ans
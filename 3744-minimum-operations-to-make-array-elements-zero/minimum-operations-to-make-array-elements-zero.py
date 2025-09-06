class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        n = len(queries)
        ans = 0
        for l, r in queries:
            tmp = l
            power = 0
            while tmp > 0:
                tmp = tmp // 4
                power += 1
            cur = 4**power
            if r < cur:
                curans = power*(r-l+1)
            else:
                curans = power*(min(cur, r) - l)
                power += 1
                nex = 4 ** power
                while nex <= r:
                    curans += power*(nex - cur)
                    cur = nex
                    power += 1
                    nex = 4**power
                curans += power*(r-cur+1)
            if curans%2 == 0:
                ans += curans//2
            else:
                ans += curans//2 + 1
        return ans
                
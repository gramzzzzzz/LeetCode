class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        m = len(languages)
        l = []
        for i in languages:
            l.append(set(i))
        tofind = []
        for x, y in friendships:
            fl = False
            for i in l[x-1]:
                if i in l[y-1]:
                    fl = True
                    break
            if not fl:
                tofind.append([x, y])
        ans = float('inf')
        for i in range(n+1):
            cnt = 0
            vis = set()
            for x, y in tofind: 
                if i not in l[x-1] and x not in vis:
                    vis.add(x)
                    cnt += 1
                if i not in l[y-1] and y not in vis:
                    vis.add(y)
                    cnt += 1
            ans = min(ans, cnt)
        return ans
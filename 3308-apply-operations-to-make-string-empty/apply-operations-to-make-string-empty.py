class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        n = len(s)
        d = Counter(s)
        # print(d)
        t = max(d.values())
        if t == 1:
            return s
        # print(t)
        ch = set()
        for i in d:
            if d[i] == t:
                ch.add(i)
        # print(ch)
        ans = ""
        for i in s:
            if d[i] == 1 and i in ch:
                ans += i
            d[i] -= 1
        return ans
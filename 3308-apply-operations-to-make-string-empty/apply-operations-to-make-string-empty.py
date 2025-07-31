class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        n = len(s)
        d = Counter(s)
        # print(d)
        t = max(d.values())
        # print(t)
        ch = set()
        for i in d:
            if d[i] == t:
                ch.add(i)
        if len(s) <= 1:
            return ''.join(list(s))
        # print(ch)
        ans = ""
        for i in s:
            if d[i] == 1 and i in ch:
                ans += i
            d[i] -= 1
        return ans
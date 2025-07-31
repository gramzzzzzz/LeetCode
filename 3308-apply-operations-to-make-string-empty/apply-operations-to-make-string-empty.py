class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        n = len(s)
        d = Counter(s)
        t = max(d.values())
        if t == 1:
            return s
        ch = set()
        for i in d:
            if d[i] == t:
                ch.add(i)
        ans = ""
        # for i in s:
        #     if d[i] == 1 and i in ch:
        #         ans += i
        #     d[i] -= 1
        for i in range(n-1, -1, -1):
            if not ch:
                break
            if s[i] in ch:
                ans += s[i]
                ch.remove(s[i])
        return ans[::-1]
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()
        if n < 2:
            return intervals

        ans = []

        st = intervals[0][0]
        en = intervals[0][1]
        for i in intervals[1:]:
            if i[0] <= en:
                en = max(i[1], en)
            else:
                ans.append([st, en])
                st = i[0]
                en = i[1]
        ans.append([st, en])
        return ans
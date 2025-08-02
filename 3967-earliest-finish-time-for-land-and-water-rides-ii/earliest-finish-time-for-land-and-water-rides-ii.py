class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        et = []
        st = []
        n = len(landStartTime)
        m = len(waterStartTime)
        for i in range(m):
            et.append((waterStartTime[i]+waterDuration[i], waterStartTime[i]))
            st.append((waterStartTime[i], waterStartTime[i]+waterDuration[i]))
        et.sort()
        st.sort()
        minet = [0] * m
        minet[-1] = st[-1][1]
        for i in range(m-2, -1, -1):
            minet[i] = min(minet[i+1], st[i][1])
        mindur = [0] * m
        mindur[0] = st[0][1]-st[0][0]
        for i in range(1, m):
            mindur[i] = min(mindur[i-1], st[i][1]-st[i][0])
        ans = float('inf')
        for i in range(n):
            start = landStartTime[i]
            end = landStartTime[i]+landDuration[i]
            stind = bisect_right(et, (start,))
            endind = bisect_left(st, (end,))
            if stind > 0:
                ans = min(ans, end)
            else:
                ans = min(ans, et[stind][0]+landDuration[i])
            if endind < m:
                ans = min(ans, minet[endind])
            if endind > 0:
                ans = min(ans, end+mindur[endind-1])
        return ans
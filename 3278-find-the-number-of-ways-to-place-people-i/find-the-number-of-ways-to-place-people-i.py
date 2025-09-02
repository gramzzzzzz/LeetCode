class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort(key=lambda x: (x[0], -x[1]))
        ans = 0
        # print(points)
        for i in range(n):
            miny = float('inf')
            for j in range(i-1, -1, -1):
                if points[j][1] < miny and points[j][1] >= points[i][1]:
                    ans += 1
                if points[j][1] >= points[i][1]:
                    miny = min(miny, points[j][1])
                # if points[i][1] <= points[j][1]:
                #     ans += 1
                #     for k in range(j+1, i):
                #         if points[i][1] <= points[k][1] <= points[j][1]:
                #             ans -= 1
                #             break
        return ans
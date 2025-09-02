class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        xs = [i[0] for i in points]
        ys = [i[1] for i in points]
        xs.sort()
        ys.sort()
        points.sort(key=lambda x: (x[0], -x[1]))
        ans = 0
        print(points, xs, ys)
        for i in range(n):
            for j in range(i-1, -1, -1):
                if points[i][1] <= points[j][1]:
                    # u = bisect_right(ys, points[j][1])
                    # d = bisect_left(ys, points[i][1])
                    # l = bisect_left(xs, points[j][0])
                    # r = bisect_right(xs, points[i][0])
                    # print(points[i], points[j], u, d, l, r)
                    # if r-l-1 <= 1 or u-d-1 <= 1:
                    #     print("YEs")
                    ans += 1
                    for k in range(j+1, i):
                        if points[i][1] <= points[k][1] <= points[j][1]:
                            ans -= 1
                            break
        return ans
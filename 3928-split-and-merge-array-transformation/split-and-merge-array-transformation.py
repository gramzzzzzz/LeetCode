class Solution:
    def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        # tar = ''.join(list(map(str, nums2)))
        tar = tuple(nums2)
        # s1 = ''.join(list(map(str, nums1)))
        s1 = tuple(nums1)
        # print(tar)

        @cache
        def helper(s1, ans):
            # print(s1)
            # print(ans)
            if s1 == tar:
                return ans
            if ans >= n:
                return float('inf')
            answer = float('inf')
            for i in range(n):
                for j in range(i, n):
                    spl = s1[i:j+1]
                    left = s1[:i]
                    right = s1[j+1:]
                    for x in range(0, i):
                        answer = min(answer, helper(left[:x] + spl + left[x:] + right , ans+1))
                    for x in range(0, n-j):
                        answer = min(answer, helper(left + right[:x] + spl + right[x:], ans+1))
            return answer

        q = deque()
        vis = set()
        vis.add(s1)
        q.append((s1, 0))
        while q:
            s1, ans = q.popleft()
            if s1 == tar:
                return ans
            # if ans >= n:
            #     continue
            for i in range(n):
                for j in range(i, n):
                    spl = s1[i:j+1]
                    left = s1[:i]
                    right = s1[j+1:]
                    for x in range(0, i):
                        tmp = left[:x] + spl + left[x:]
                        if tmp not in vis:
                            q.append((tmp , ans+1))
                            vis.add(tmp)
                    for x in range(0, n-j):
                        tmp = left + right[:x] + spl + right[x:]
                        if tmp not in vis:
                            q.append((tmp, ans+1))
                            vis.add(tmp)
        return 0
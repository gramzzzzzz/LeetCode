class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def eval(arr):
            st = []
            for i in arr:
                if i in ['*', '-', '+', '/']:
                    if len(st) < 2:
                        return False
                    b = st.pop()
                    a = st.pop()
                    if i == '*':
                        ans = (a*b)
                    elif i == '+':
                        ans = (a+b)
                    elif i == '-':
                        ans = (a-b)
                    else:
                        if b == 0:
                            return False
                        ans = (a/b)
                    st.append(ans)
                else:
                    st.append(i)
            if len(st) > 1:
                return False
            return 23.991 <= st[0] <= 24.001

        vis = set()
        arr = []
        def helper(cnt):
            if cnt == 7:
                if len(arr) > 1:
                    return False
                # print(arr)
                return 23.991 <= arr[0] <= 24.001
            # if len(arr) == 7:
            #     return eval(arr)
            ans = False
            for i in range(4):
                if i not in vis:
                    vis.add(i)
                    arr.append(cards[i])
                    ans |= helper(cnt+1)
                    arr.pop()
                    vis.remove(i)
            if len(arr) >= 2:
                for i in ['*', '-', '+', '/']:
                    b = arr.pop()
                    a = arr.pop()
                    if i == '*':
                        res = (a*b)
                    elif i == '+':
                        res = (a+b)
                    elif i == '-':
                        res = (a-b)
                    else:
                        if b == 0:
                            arr.append(a)
                            arr.append(b)
                            continue
                        res = (a/b)
                    arr.append(res)
                    ans |= helper(cnt+1)
                    arr.pop()
                    arr.append(a)
                    arr.append(b)
            return ans

        return helper(0)
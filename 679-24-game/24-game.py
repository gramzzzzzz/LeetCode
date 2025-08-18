class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def eval(arr):
            st = []
            for i in arr:
                if i in ['*', '-', '+', '/']:
                    # print(len(arr))
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
        def helper():
            if len(arr) == 7:
                # if arr[0] == 9 and arr[1] == 1:
                    # print(arr)
                return eval(arr)
            ans = False
            for i in range(4):
                if i not in vis:
                    vis.add(i)
                    arr.append(cards[i])
                    ans |= helper()
                    arr.pop()
                    vis.remove(i)
            if len(arr) >= 2:
                for i in ['*', '-', '+', '/']:
                    arr.append(i)
                    ans |= helper()
                    arr.pop()
            return ans

        return helper()
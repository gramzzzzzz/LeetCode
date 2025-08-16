class Solution:
    def minSensors(self, n: int, m: int, k: int) -> int:
        k *= 2
        k += 1
        # print(k)
        ans = (m//k) + int(m%k!=0)
        # print(ans, int(m%k==1))
        ans *= ((n//k) + int(n%k!=0))
        return ans
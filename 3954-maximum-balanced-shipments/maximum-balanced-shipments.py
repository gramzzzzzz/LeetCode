class Solution:
    def maxBalancedShipments(self, weights: List[int]) -> int:
        n = len(weights)
        cnt = 0
        i = 1
        while i < n:
            if weights[i] < weights[i-1]:
                cnt += 1
                i += 1
            i += 1
        return cnt
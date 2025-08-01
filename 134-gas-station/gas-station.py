class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if sum(gas) < sum(cost):
            return -1
        surplus = 0
        start = 0
        for i in range(n):
            surplus += gas[i]-cost[i]
            if surplus < 0:
                start = i+1
                surplus = 0
        return start
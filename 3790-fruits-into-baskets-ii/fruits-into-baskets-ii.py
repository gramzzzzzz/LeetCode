class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        unplaced = set()
        taken = set()
        for i in range(n):
            flag = False
            for j in range(n):
                if j not in taken and baskets[j] >= fruits[i]:
                    taken.add(j)
                    flag = True
                    break
            if not flag:
                unplaced.add(i)
        return len(unplaced)
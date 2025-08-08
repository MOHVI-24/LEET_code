from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        fruits.sort()
        baskets.sort()
        i = j = 0
        n, m = len(fruits), len(baskets)
        unplaced = 0
        while i < n and j < m:
            if baskets[j] >= fruits[i]:
                i += 1
                j += 1
            else:
                j += 1
        unplaced = n - i
        return unplaced

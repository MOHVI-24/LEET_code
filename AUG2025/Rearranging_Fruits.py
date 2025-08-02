from collections import Counter
from typing import List

# code for leetcode 
class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        c1 = Counter(basket1)
        c2 = Counter(basket2)
        total = c1 + c2

        if any(v % 2 != 0 for v in total.values()):
            return -1

        need = []
        for fruit in total:
            diff = c1[fruit] - total[fruit] // 2
            if diff > 0:
                need.extend([fruit] * diff)
            elif diff < 0:
                need.extend([fruit] * (-diff))

        need.sort()
        min_fruit = min(basket1 + basket2)

        swaps = len(need) // 2
        x = sum(min(need[i], 2 * min_fruit) for i in range(swaps))
        return x
    


"""basket1 = [4,2,2,2]
basket2 = [1,4,1,2]

cost = 0

for i in range (0,len(basket1)):
    for j in range (0,len(basket2)):
        
        basket1[i], basket2[j] = basket2[j],basket1[i]

        if basket1 == basket2:
            cost += 1
    print(cost)"""


"""from collections import Counter

def minCostToMakeBasketsEqual(basket1, basket2):
    count1 = Counter(basket1)
    count2 = Counter(basket2)
    
    total_count = Counter()
    for fruit in set(basket1 + basket2):
        total = count1[fruit] + count2[fruit]
        if total % 2 != 0:
            return -1  # Can't balance
        total_count[fruit] = total // 2
    
    diff = Counter()
    for fruit in total_count:
        if count1[fruit] > total_count[fruit]:
            diff[fruit] = count1[fruit] - total_count[fruit]

    # Now create the list of extra elements to swap
    to_swap = []
    for fruit in diff:
        to_swap.extend([fruit] * diff[fruit])

    to_swap.sort()  # For minimal cost
    min_elem = min(basket1 + basket2)
    cost = 0
    
    for i in range(len(to_swap) // 2):
        cost += min(to_swap[i], 2 * min_elem)

    return cost"""

"""
from collections import Counter
class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        
            freq = Counter(b1) + Counter(b2)
            if any(v % 2 for v in freq.values()):
                return -1  # Impossible case

            need = Counter()
            for k in freq:
                diff = Counter(b1)[k] - freq[k] // 2
                if diff > 0: need += Counter({k: diff})

    swap = sorted(need.elements())
    m = min(b1 + b2)
    return sum(min(x, 2*m) for x in swap[:len(swap)//2])"""


""""""
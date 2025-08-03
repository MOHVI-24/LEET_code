from typing import List

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        positions = [pos for pos, _ in fruits]
        prefix = [0] * (n + 1)
        
        for i in range(n):
            prefix[i + 1] = prefix[i] + fruits[i][1]
        
        def get_sum(i, j):
            return prefix[j + 1] - prefix[i]

        max_fruits = 0
        l = 0

        for r in range(n):
            # Move window from l to r
            while l <= r:
                left_pos = fruits[l][0]
                right_pos = fruits[r][0]

                # Distance needed to walk:
                min_dist = min(
                    abs(startPos - left_pos) + (right_pos - left_pos),
                    abs(startPos - right_pos) + (right_pos - left_pos)
                )

                if min_dist <= k:
                    max_fruits = max(max_fruits, get_sum(l, r))
                    break
                l += 1
        
        return max_fruits




































"""from typing import List
class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        pos, amt = zip(*fruits); pre = [0]; [pre.append(pre[-1] + x) for x in amt]
        return max(pre[r+1]-pre[l] for l in range(len(fruits)) for r in range(l, len(fruits))
                   if min(abs(startPos - pos[l]) + (pos[r] - pos[l]), abs(startPos - pos[r]) + (pos[r] - pos[l])) <= k)
"""
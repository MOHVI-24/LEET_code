
from typing import List

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:

        nums.sort()

        n = len(nums)

        maxlen = 0 
        left = 0 

        for right in range(n):

            while nums [right] > nums [left] * k : 
                left += 1 

            maxlen = max(maxlen , right - left + 1)

        x = n -maxlen 

        return x 
    
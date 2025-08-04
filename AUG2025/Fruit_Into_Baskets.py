from collections import defaultdict
from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_count = defaultdict(int)
        left = 0
        max_len = 0

        for right in range(len(fruits)):
            fruit_count[fruits[right]] += 1

            # Shrink window if there are more than 2 types of fruits
            while len(fruit_count) > 2:
                fruit_count[fruits[left]] -= 1
                if fruit_count[fruits[left]] == 0:
                    del fruit_count[fruits[left]]
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
      
        
        
        
        
        
        
        
        
        
        
        
        
        
        """count = 0
        for i in range(len(fruits)):

            if (i.isnumeric()):

                count += 1

                return count 
        
        return 0 """
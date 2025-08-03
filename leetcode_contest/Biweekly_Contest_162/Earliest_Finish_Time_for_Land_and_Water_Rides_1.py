from typing import List


class Solution:
    def earliestFinishTime(
        self, 
        landStartTime: List[int], landDuration: List[int],
        waterStartTime: List[int], waterDuration: List[int]
    ) -> int:
        
        res = float('inf')
        n, m = len(landStartTime), len(waterStartTime)
        
        for i in range(n):
            for j in range(m):
                start_land = landStartTime[i]
                end_land = start_land + landDuration[i]
                start_water = max(waterStartTime[j], end_land)
                end1 = start_water + waterDuration[j]
                

                start_water = waterStartTime[j]
                end_water = start_water + waterDuration[j]
                start_land = max(landStartTime[i], end_water)
                end2 = start_land + landDuration[i]
                
                res = min(res, end1, end2)
        
        return res

class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        count = 0
        start = 0
        cur_max = weight[0]

        for i in range(1, len(weight)):
            cur_max = max(cur_max, weight[i])
            if weight[i] < cur_max:
                count += 1
                start = i + 1
                if start < len(weight):
                    cur_max = weight[start]
        return count

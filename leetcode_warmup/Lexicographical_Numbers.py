class Solution:
    def lexicalOrder(self, n: int): #-> List[int]:
        
        list1 = []
        """current = 1 
        while len(list1) < n :
            list1.append(current)
            
            if current * 10 <= n:
                current * 10                                        # my apporach 
            else :
                while (current == n) or (current % 10 == 9):
                     current = current // 10 
                current += 1
                
        return list1"""


        #dfs apporch

        #list1 = []
        def dfs(current):
            if current > n :
                return 
            list1.append(current)
            for i in range (10):
                dfs(current * 10 + i)
                
        for j in range (1,10):
            dfs (j)

        return list1
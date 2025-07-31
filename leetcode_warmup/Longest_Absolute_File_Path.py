class Solution:
    def lengthLongestPath(self, input: str) -> int:
        maxL = 0
        path = {0: 0}

        for line in input.split('\n'):
            name = line.lstrip('\t')
            go = len(line) - len(name)

            if '.' in name:
                maxL = max(maxL, path[go] + len(name))
            else:
                path[go + 1] = path[go] + len(name) + 1 
        
        return maxL
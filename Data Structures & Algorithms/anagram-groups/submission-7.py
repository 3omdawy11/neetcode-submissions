from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mp = defaultdict(list)

        for i in range(len(strs)):
            s = "".join(sorted(strs[i]))
            
            mp[s].append(i)

        #print(mp)

        l = []
        for key, lst in mp.items():
            currentL = []
            for v in lst:
                currentL.append(strs[v])
                #print(currentL)
            
            l.append(currentL)

        return l
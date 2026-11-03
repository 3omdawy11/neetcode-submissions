from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = defaultdict(list)

        for s in strs:
            alphabets = [0] * 26
            for c in s:
                index = ord(c) - ord('a')
                alphabets[index] += 1
            
            alphabets = tuple(alphabets)
            ans[alphabets].append(s)

        print(ans.values())
        return list(ans.values())
        

        
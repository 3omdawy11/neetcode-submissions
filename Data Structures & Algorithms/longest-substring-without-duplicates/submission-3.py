class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0  


        for i in range(len(s)):
    

            counter = 0
            m = {}
            

            for j in range(i, len(s)):
                if s[j] in m:
                    
                    break
                else:
                    m[s[j]] = 1
                    counter += 1
            ans = max(ans, counter)
        return ans
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0:
            return 0

        m = {}

        left, right = 0, 1
        m[s[left]] = left
        mx = 1
        while right < len(s):

            fChar = s[right]
            if fChar in m:
                while fChar in m:
                    m.pop(s[left])
                    left += 1
                m[fChar] = right
                #print(m)
                # left += 1
            
            else:
                m[fChar] = right
                mx = max(mx, right - left + 1)
            
            right += 1

        return mx
        
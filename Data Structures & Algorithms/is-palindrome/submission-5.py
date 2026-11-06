class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(" ", "")

        l, r = 0, len(s) - 1

        while l < r:
            while not s[r].isalpha() and not s[r].isdigit() and l < r:
                r -= 1
            while not s[l].isalpha() and not s[l].isdigit() and l < r:
                l += 1
            
            if l > r:
                return False

            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True
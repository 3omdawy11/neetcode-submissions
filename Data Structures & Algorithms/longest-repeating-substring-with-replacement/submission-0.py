class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}
        l,r = 0, 0
        mx = 0

        while r < len(s):

            count[s[r]] = 1 + count.get(s[r], 0)

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l+= 1


            mx = max(mx, r - l + 1)
            # print(mx)

            r += 1

        return mx
        
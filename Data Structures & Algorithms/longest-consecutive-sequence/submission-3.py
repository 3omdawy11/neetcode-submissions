from sortedcontainers import SortedSet
from collections import Counter
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #counter_dict = Counter(nums)
        s = SortedSet(nums)
        if not nums:
            return 0
        mx = 1
        counter = 1
        print(s)
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                counter += 1
            elif s[i] == s[i-1] + 1:
                counter += 1
            else:
                mx = max(mx, counter)
                counter = 1
        mx = max(mx, counter)
        return mx   
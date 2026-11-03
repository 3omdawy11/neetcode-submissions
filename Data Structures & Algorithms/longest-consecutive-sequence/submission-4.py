from sortedcontainers import SortedSet
from collections import Counter
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #counter_dict = Counter(nums)
        mx = 0
        
        s = set(nums)
        for number in nums:
            counter = 0
            if number - 1 not in s:
                while number in s:
                    counter += 1
                    number += 1
                
                mx = max(mx, counter)

        return mx
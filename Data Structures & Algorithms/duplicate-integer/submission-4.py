class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp = {}
        for i in nums:
            mp[i] = mp.get(i, 0) + 1
            if mp[i] == 2:
                return True
        return False
        
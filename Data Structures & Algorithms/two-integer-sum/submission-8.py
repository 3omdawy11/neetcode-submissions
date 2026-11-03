class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mp = {}
        counter = 0
        for i in nums:
            mp[i] = counter
            counter += 1
        counter = 0
        l = []
        for i in nums:
            if (target - i) in mp:
                if counter != mp[target - i]:
                    return [counter, mp[target - i]]
            counter += 1
        return []
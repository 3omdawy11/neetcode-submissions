class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if len(nums) == 2:
            return min(nums[0], nums[1])

        l,r = 0, len(nums) - 1
        ans = nums[0]
        #mid = 0

        while l <= r:
            
            mid = (l + r) // 2
            if nums[mid] >= nums[l] and nums[mid] >= nums[r]:
                l = mid + 1

            else:
                r = mid - 1
            
            ans = min(ans,nums[mid])
            
        #ans = min(ans,nums[mid])

        return ans
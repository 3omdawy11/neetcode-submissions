class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0

        nums = sorted(nums)

        counter = 1
        previous = nums[0]

        mx = counter

        for current in nums[1::]:
            #print(current, previous)

            if current == previous:
                continue
            
            if current == previous + 1:
                counter += 1

            else:
                mx = max(mx, counter)
                counter = 1

            previous = current    

        mx = max(mx, counter)
        
        # print(nums[1::])

        return mx
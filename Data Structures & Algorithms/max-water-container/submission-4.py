class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l, r = 0, len(heights) - 1
        mx = 0

        while l < r:
            num = (r - l) * min(heights[r], heights[l])
            
            if num > mx:
                mx = num
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return mx
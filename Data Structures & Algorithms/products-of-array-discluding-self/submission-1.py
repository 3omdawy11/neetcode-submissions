class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ll, lr = [1], [1]

        for n in nums:
            ll.append(ll[-1] * n)

        for n in nums[::-1]:
            lr.append(lr[-1] * n)

        ll.append(1)
        lr.append(1)

        lr = lr[::-1]
        
        

        #print(ll,lr)

        i = 1

        ans = []

        while i <= len(nums):
            ans.append(ll[i - 1] * lr[i + 1])

            i+=1


        return ans
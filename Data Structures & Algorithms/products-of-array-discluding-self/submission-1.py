class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #lets use prefix/suffix pattern 

        n = len(nums)
        res = [0] * n

        #Product of left side , prefix 

        prefix = 1
        for i in range(n):
            res[i] = prefix 
            prefix *= nums[i]

        #product of right side , suffix 

        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)

        for left in range(len(nums)):
            product = 1
            for right in range(len(nums)):
                if right == left:
                    continue
                product *= nums[right]
            result[left] = product

        return result 


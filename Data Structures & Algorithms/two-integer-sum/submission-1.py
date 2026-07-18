class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}
        for i in range(len(nums)):
            ans = target - nums[i]
            if ans in maps:
                return [maps[ans], i]
            maps[nums[i]] = i

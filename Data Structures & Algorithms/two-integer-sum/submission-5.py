class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if nums[i] in differences:
                return [differences[nums[i]], i]
            differences[difference] = i
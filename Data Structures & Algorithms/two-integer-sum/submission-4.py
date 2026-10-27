class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            differences[difference] = i

        for j in range(len(nums)):
            if nums[j] in differences:
                if j != differences[nums[j]]:
                    return [j, differences[nums[j]]]
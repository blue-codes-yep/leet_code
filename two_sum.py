class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp_dict = dict()
        temp_dict[nums[0]] = None
        for i in range(1, len(nums)):
            if target - nums[i] in temp_dict:
                return nums.index(target - nums[i]), i
            else:
                temp_dict[nums[i]] = None

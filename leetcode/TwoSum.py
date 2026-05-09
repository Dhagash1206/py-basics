class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        need = {}

        for index in range(len(nums)):
            need[nums[index]] = index

        for index in range(len(nums)):
            current_number = nums[index]
            more = target - current_number

            if more in need and need[more] != index:
                return [index, need[more]]

        return []
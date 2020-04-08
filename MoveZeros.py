class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_number_index = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            else:
                if (i-1 == last_number_index):
                    last_number_index += 1
                    continue
                else:
                    last_number_index += 1
                    nums[last_number_index], nums[i] = nums[i], nums[last_number_index]
        return nums

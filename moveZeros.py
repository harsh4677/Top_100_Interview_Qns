class Solution(object):
    def moveZeroes(self, nums):
        non_zero_index = 0  # Points to the position where the next non-zero element should be placed

        for i in range(len(nums)):
            if nums[i] != 0:
                # Swap the current non-zero element with the element at non_zero_index
                nums[i], nums[non_zero_index] = nums[non_zero_index], nums[i]
                non_zero_index += 1


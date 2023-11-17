class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        expected_sum = n * (n + 1) // 2  # The sum of all numbers from 0 to n
        actual_sum = sum(nums)  # The sum of numbers in the given array
        missing_number = expected_sum - actual_sum
        return missing_number
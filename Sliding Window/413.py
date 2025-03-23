class Solution:
    def numberOfArithmeticSlices(self, nums):
        if len(nums) < 3:
            return 0

        count = 0
        length = 2

        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                length += 1
                count += (length - 2)

            else:
                length = 2

        return count
class Solution:
    def minOperations(self, nums):
        length = len(nums)
        operations = 0

        for i in range(length - 2):
            if nums[i] == 0:
                nums[i] ^= 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1

                operations += 1
            
        return operations if all(x == 1 for x in nums) else -1
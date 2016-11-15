class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        if len(nums) == 1:
            return nums[0]
        if nums[0] != nums[1] and nums[1] == nums[2]:
            return nums[0]
        if nums[len(nums) - 1] != nums[len(nums) -2] and nums[len(nums)-2] == nums[len(nums)-3]:
            return nums[len(nums) - 1]
        for i in range(1,len(nums)):
            if nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
                return nums[i]

solution = Solution()
print(solution.singleNumber([1, 2, 1, 2, 3, 4, 4, 1, 2, 4]))

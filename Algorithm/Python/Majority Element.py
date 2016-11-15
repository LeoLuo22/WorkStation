class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        flag = len(nums) // 2
        tmp = nums[0]
        count = 1
        for i in range(0, len(nums)):
            if count > flag:
                return tmp
            if tmp == nums[i + 1]:
                count += 1
            else:
                tmp = nums[i + 1]
                count = 1
        #69ms

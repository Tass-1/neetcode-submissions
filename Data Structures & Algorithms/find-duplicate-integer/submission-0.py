class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        see = set()
        for i in range(len(nums)):
            if(nums[i]) in see:
                return nums[i]
            else:
                see.add(nums[i])
        return 1
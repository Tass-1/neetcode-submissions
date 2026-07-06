class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            temp = 1
            for j in range (1,len(nums)):
                temp = temp*nums[j]
            res.append(temp)
            nums = nums[1:] + nums[:1]
        return res
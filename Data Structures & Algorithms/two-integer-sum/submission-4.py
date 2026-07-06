class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range (0, len(nums)):
            tbf = target -nums[i]
            if( tbf in nums[i+1:] ):
                return [i , nums[i+1:].index(tbf) + (i+1)]
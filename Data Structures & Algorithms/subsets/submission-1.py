class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sub = []
        res = []
        
        def btx(i):
            if i>= len(nums):
                res.append(sub.copy())
                return
            sub.append(nums[i])
            btx(i+1)
            sub.pop()
            btx(i+1)
        btx(0)
        return res

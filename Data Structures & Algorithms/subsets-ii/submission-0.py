class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        c= []
        nums.sort()
        print(nums)
        def bt(i):
            if i>=len(nums):
                if c in nums:
                    return
                res.append(c.copy())
                return
            c.append(nums[i])
            bt(i+1)
            c.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            bt(i+1)
        bt(0)
        print(res)
        return(res)
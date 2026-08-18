class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        c = []
        def bt():
            if len(c) == len(nums):
                res.append(c.copy())
                return
            for n in nums:
                if n in c:
                    continue
                c.append(n)
                bt()
                c.pop()
            
            
        bt()
        print(res)
        return res

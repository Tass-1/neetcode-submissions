class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k-1
        lis = []
        while( r < len(nums)):
            m = max(nums[l:r+1])
            lis.append(m)
            l = l+1
            r =r+1
        return lis
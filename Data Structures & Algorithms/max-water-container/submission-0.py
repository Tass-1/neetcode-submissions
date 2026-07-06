class Solution:
    def maxArea(self, heights: List[int]) -> int:
        le = 0
        ri = len(heights) -1
        res = 0
        while(le < ri):
            diff = ri - le
            hi = min(heights[le] , heights[ri])
            water = diff * hi
            res = max(res, water)
            if(le+1 == ri):
                le = le +1
                ri = len(heights) -1
            else:
                ri = ri -1
        return res
        
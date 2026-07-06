class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        mlh = 0
        mrh = 0
        le =  0
        ri = len(height) -1
        while( le < ri):
            if(height[le] < height[ri]):
                if( height[le] >= mlh ):
                    mlh = height[le]
                    le = le +1
                else:
                    area = mlh - height[le]
                    water = water + area
                   
                    mlh = max(mlh , height[le])
                    le = le +1
            else:
                if( height[ri] >= mrh):
                    mrh = height[ri]
                    ri = ri -1
                else:
                    area = mrh - height[ri]
                    water = water + area
                    ri = ri -1
        return water 
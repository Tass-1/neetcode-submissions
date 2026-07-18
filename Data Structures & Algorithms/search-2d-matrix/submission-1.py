class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            lis = matrix[i]
            l = 0
            r = len(lis)-1
            while( l <= r):
                mid = l + (r-l)//2
                if( target == lis[mid]):
                    return True
                elif( target > lis[mid]):
                    l = l + 1
                else:
                    r = r - 1
        return False
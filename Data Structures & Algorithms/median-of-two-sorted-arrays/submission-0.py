class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        k = nums1 + nums2
        k = sorted(k)
        m = len(k)
        l= 0
        r = m-1
        mid = l + (r-l)//2
        if( m%2 != 0):
            print(k)
            return k[mid]
        else:
            return ((k[mid]+k[mid+1])/2)

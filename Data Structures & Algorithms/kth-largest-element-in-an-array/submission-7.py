import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        minh = []
        for j in range(len(nums)):
            heapq.heappush(minh , nums[j])
            if len(minh) > k:
                heapq.heappop(minh)
       
        return minh[0]
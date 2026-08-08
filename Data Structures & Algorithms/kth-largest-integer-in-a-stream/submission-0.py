import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.himin = nums
        heapq.heapify(self.himin)

        while len(self.himin) > self.k:
            heapq.heappop(self.himin)

        
    def add(self, val: int) -> int:
        heapq.heappush(self.himin , val)
        if len(self.himin) > self.k:
            heapq.heappop(self.himin)
        
        return self.himin[0]

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        best = high

        while low <= high:
            totalhr = 0
            mid = (low+high) // 2
            for pile in piles:
                totalhr += math.ceil(pile/mid)
            if totalhr <= h:
                best = mid
                high = mid - 1
            else:
                low = mid+1

        return best
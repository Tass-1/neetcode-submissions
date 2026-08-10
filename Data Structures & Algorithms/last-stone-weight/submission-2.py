class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        i = 0
        j = 1
        while (len(stones) > 1):
            b = stones.copy()
            
            ch2 = max(b)
            b.remove(ch2)
            ch1 = max(b)
            if ch1>ch2:
                stones.remove(ch1) 
                stones.remove(ch2)
                stones.insert(0,ch1 - ch2)
            elif ch2 > ch1:
                print(stones)
                print(ch1)
                print(ch2)
                stones.remove(ch1)
                stones.remove(ch2)
                stones.insert(0,ch2-ch1)
            else:
                print(stones)
                print(ch1)
                print(ch2)
                stones.remove(ch1)
                stones.remove(ch2)
        if stones:
            return stones[0]
        else:
            return 0
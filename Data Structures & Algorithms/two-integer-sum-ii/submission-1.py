class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        for i in range (len(numbers)):
            val = target - numbers[i]
            if(i == len(numbers)):
                break
            for j in range (i+1, len(numbers)):
                if(numbers[j] == val):
                    res.append(i+1)
                    res.append(j+1)

        return res
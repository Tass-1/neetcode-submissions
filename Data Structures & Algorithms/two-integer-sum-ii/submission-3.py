class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            nu = numbers[i]
            tbf = target - nu
            if(tbf in numbers[i:]):
                return [i+1 , numbers[i:].index(tbf) + i+1]
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftPtr = 0
        rightPtr = len(numbers) - 1

        while (rightPtr > leftPtr):
            total = numbers[leftPtr] + numbers[rightPtr]
            if total < target:
                leftPtr += 1
            elif total > target:
                rightPtr -= 1
            else:
                return [leftPtr + 1, rightPtr + 1]

        return []

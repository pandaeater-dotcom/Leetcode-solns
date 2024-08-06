class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCt = 0
        prod = 1
        answer = []
        for num in nums:
            if (num == 0):
                zeroCt += 1
            else:
                prod *= num
        
        for num in nums:
            if num == 0: 
                if zeroCt <= 1:
                    answer.append(prod)
                else:
                    answer.append(0)
            elif zeroCt:
                answer.append(0)
            else:
                answer.append(prod // num)
        
        return answer

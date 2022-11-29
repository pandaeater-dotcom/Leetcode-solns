class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        if len(num) == k:
            return "0"
        for x in num:
            while (len(stack) > 0 and int(stack[len(stack)-1]) > int(x) and k > 0):
                k -= 1
                stack.pop()
            stack.append(x)
        while (k > 0):
            stack.pop()
            k -= 1
        return str(int("".join(stack)))

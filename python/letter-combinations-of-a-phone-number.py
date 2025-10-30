class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combinations = []
        hashMap = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        def recursiveBacktrack(startIndex: int = 0, path: str = ""):
            if len(path) == len(digits):
                combinations.append(path)
                return

            for char in hashMap[digits[startIndex]]:
                recursiveBacktrack(startIndex + 1, path + char)

        recursiveBacktrack()
        return combinations

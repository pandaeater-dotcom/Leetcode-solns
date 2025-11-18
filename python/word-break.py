class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        options = defaultdict(set)
        for word in wordDict:
            options[len(word)].add(word)
        cache = [False] * len(s)
        optionItems = sorted(options.items())
        for i in range(len(s)):
            substring = s[:i + 1]
            iter = 0
            while iter < len(optionItems) and len(substring) >= optionItems[iter][0]:
                length = optionItems[iter][0]
                for word in optionItems[iter][1]:
                    if substring == word or cache[len(substring) - 1 - length] and substring[-length:] == word:
                        cache[len(substring) - 1] = True
                iter += 1

        return cache[-1]

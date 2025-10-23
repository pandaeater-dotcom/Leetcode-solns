class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        refFreq = Counter(s1)
        curFreq = defaultdict(int)

        left = 0
        for right in range(len(s2)):
            curFreq[s2[right]] += 1
            if right - left + 1 < len(s1):
                continue

            isPerm = curFreq == refFreq
            if isPerm:
                return True

            if curFreq[s2[left]] > 1:
                curFreq[s2[left]] -= 1
            else:
                del curFreq[s2[left]]
            left += 1

        return False

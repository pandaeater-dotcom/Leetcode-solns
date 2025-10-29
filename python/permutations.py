class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []

        def recursiveBacktrack(rem: Set[int], currElems: List[int]):
            if not rem:
                perms.append(currElems[:])
                return

            for index, num in enumerate(rem):
                currElems.append(num)
                rem.remove(num)
                recursiveBacktrack(rem.copy(), currElems)
                rem.add(num)
                currElems.pop()

        recursiveBacktrack(set(nums), [])
        return perms

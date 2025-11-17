class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list[int])
        indegs = [0] * numCourses

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegs[course] += 1

        taken = 0
        q = deque([x for x in range(numCourses) if not indegs[x]])
        while q:
            elem = q.popleft()
            for seq in adj[elem]:
                indegs[seq] -=1
                if not indegs[seq]:
                    q.append(seq)
            taken += 1

        return taken == numCourses

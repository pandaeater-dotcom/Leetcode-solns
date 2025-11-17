class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list[int])
        indegs = [0] * numCourses

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegs[course] += 1

        order = []
        q = deque([x for x in range(numCourses) if not indegs[x]])
        while q:
            elem = q.popleft()
            for seq in adj[elem]:
                indegs[seq] -= 1
                if not indegs[seq]:
                    q.append(seq)
            order.append(elem)

        return order if len(order) == numCourses else []

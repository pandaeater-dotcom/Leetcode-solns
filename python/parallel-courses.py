class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adjList = defaultdict(list)
        indeg = defaultdict(int)

        for prereq, course in relations:
            adjList[prereq].append(course)
            indeg[course] += 1

        q = deque([course for course in adjList.keys() if not indeg[course]])
        if not q:
            return -1
        temp = deque()
        visited_counter = len(q)
        sems = 0

        while q:
            course = q.popleft()

            for next_course in adjList[course]:
                indeg[next_course] -= 1
                if not indeg[next_course]:
                    temp.append(next_course)
                    visited_counter += 1
            if not q:
                sems += 1
                q = temp
                temp = deque()

        if visited_counter == len(adjList):
            return sems
        else:
            return -1

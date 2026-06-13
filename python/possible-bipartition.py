class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adjList= [[] for _ in range(n)]
        colors = {}
        BLUE, RED = -1, 1

        for pair in dislikes:
            adjList[pair[0] - 1].append(pair[1])
            adjList[pair[1] - 1].append(pair[0])

        q = deque()

        for i in range(1, n+1):
            if i not in colors:
                colors[i] = BLUE
                q.append(i)
            while q:
                num = q.popleft()
                color = colors[num]
                other = color * -1

                for dislike in adjList[num - 1]:
                    if dislike not in colors:
                        colors[dislike] = other
                        q.append(dislike)
                    elif colors[dislike] == color:
                        return False
        return True

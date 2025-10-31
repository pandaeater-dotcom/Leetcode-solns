class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def getDistance(x: int, y: int) -> float:
            return sqrt(x**2 + y**2)

        distanceMap = defaultdict(list)
        distances = []
        for point in points:
            distance = getDistance(point[0], point[1])
            distanceMap[distance].append(point)
            distances.append(distance)
        heapify(distances)
        closest = []
        while k > 0:
            curIndex = 0
            while k and distances and curIndex < len(distanceMap[distances[0]]):
                closest.append(distanceMap[distances[0]][curIndex])
                k -= 1
                curIndex += 1
            heappop(distances)
        return closest

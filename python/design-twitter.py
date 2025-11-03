class Twitter:

    def __init__(self):
        self.subscribedTo = defaultdict(set[int])
        self.tweets = defaultdict(list[tuple[int, int]])
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1
        self.subscribedTo[userId].add(userId)

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        for poster in self.subscribedTo[userId]:
            for tweet in self.tweets[poster]:
                if len(minHeap) < 10 or minHeap[0][0] < tweet[0]:
                    heappush(minHeap, (tweet[0], tweet[1]))
                if len(minHeap) > 10:
                    heappop(minHeap)

        minHeap.sort(key=lambda x: x[0], reverse=True)
        return [elem[1] for elem in minHeap]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.subscribedTo[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId == followerId:
            return
        if followeeId in self.subscribedTo[followerId]:
            self.subscribedTo[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

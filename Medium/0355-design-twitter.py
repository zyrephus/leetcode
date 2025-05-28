class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list) # userId: list of (time, tweetId)
        self.follows = defaultdict(set) # userId: set of followees

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

        self.follows[userId].add(userId) # User follows themselves

    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap = []
        followees = self.follows.get(userId, set())

        for uId in followees:
            # Get last 10 tweets per followee
            for time, tweetId in self.tweets.get(uId, [])[-10:]:
                heapq.heappush(min_heap, (time, tweetId))

                if len(min_heap) > 10:
                    heapq.heappop(min_heap)
        
        res = []
        while min_heap:
            res.append(heapq.heappop(min_heap)[1])

        return res[::-1] # Reverse to get descending order in terms of time

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

class Twitter {
private:
  unordered_map<int, vector<pair<int, int>>> tweets;
  unordered_map<int, unordered_set<int>> follows;
  int inc = 0;

  struct Compare {
    bool operator()(tuple<int, int, int>& a, tuple<int, int, int>& b) {
      return get<0>(a) < get<0>(b);
    }
  };
public:
  Twitter() {}
  
  void postTweet(int userId, int tweetId) {
    tweets[userId].push_back({tweetId, inc++});
  }
  
  vector<int> getNewsFeed(int userId) {
    priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, Compare> maxHeap;
    vector<int> topTenTweets;

    if (!tweets[userId].empty()) maxHeap.push({tweets[userId].back().second, userId, tweets[userId].size() - 1});
    for (int followee : follows[userId]) {
      if (tweets[followee].empty()) continue;
      maxHeap.push({tweets[followee].back().second, followee, tweets[followee].size() - 1});
    }

    while (topTenTweets.size() < 10 && !maxHeap.empty()) {
      auto [tweet, poster, index] = maxHeap.top();
      maxHeap.pop();
      topTenTweets.push_back(tweets[poster][index].first);
      if (index) {
        maxHeap.push({tweets[poster][index - 1].second, poster, index - 1});
      }
    }

    return topTenTweets;
  }
  
  void follow(int followerId, int followeeId) {
   follows[followerId].insert(followeeId); 
  }
  
  void unfollow(int followerId, int followeeId) {
    if (follows[followerId].contains(followeeId)) {
      follows[followerId].erase(followeeId);
    }
  }
};

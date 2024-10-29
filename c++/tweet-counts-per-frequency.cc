class TweetCounts {
private:
  unordered_map<string, vector<int>> tweets;

  int getDivisor(string freq) {
    if (freq == "minute") return 60;
    else if (freq == "hour") return 60 * 60;
    else return 60 * 60 * 24;
  }
public:
  TweetCounts() {}
  
  void recordTweet(string tweetName, int time) {
    tweets[tweetName].push_back(time);
  }
  
  vector<int> getTweetCountsPerFrequency(string freq, string tweetName, int startTime, int endTime) {
    int divisor = getDivisor(freq);
    vector<int> counts((endTime - startTime) / divisor + 1, 0);
    for (const auto& time : tweets[tweetName]) {
      if (time < startTime || time > endTime) continue;
      int index = (time - startTime) / divisor;
      if (index >= counts.size()) continue;
      counts[index]++;
    }

    return counts;
  }
};

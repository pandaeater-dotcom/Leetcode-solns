class AuthenticationManager {
private:
  int ttl;
  int curT;
  unordered_map<string, int> tokens;
public:
  AuthenticationManager(int timeToLive): ttl{timeToLive}, curT{0} {}
  
  void generate(string tokenId, int currentTime) {
    tokens[tokenId] = currentTime + ttl;
  }
  
  void renew(string tokenId, int currentTime) {
    if (!tokens.contains(tokenId)) return;
    if (currentTime >= tokens[tokenId]) return;
    tokens[tokenId] = currentTime + ttl;
  }
  
  int countUnexpiredTokens(int currentTime) {
    int counter = 0;
    for (const auto& [token, time] : tokens) {
      if (currentTime < time) counter++;
    }
    return counter;
  }
};

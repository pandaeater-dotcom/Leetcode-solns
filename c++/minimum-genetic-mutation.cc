class Solution {
public:
  bool validMutation(string g1, string g2) {
    bool mutated = false;
    for (int i = 0; i < 8; ++i) {
      if (g1[i] == g2[i]) continue;
      if (mutated) return false;
      mutated = true;
    }
    return true;
  }

  int minMutation(string startGene, string endGene, vector<string>& bank) {
    unordered_map<string, vector<string>> adjList;
    if (find(bank.begin(), bank.end(), startGene) == bank.end()) bank.push_back(startGene);
    if (find(bank.begin(), bank.end(), endGene) == bank.end()) return -1;

    for (int i = 0; i < bank.size(); ++i) {
      for (int j = i + 1; j < bank.size(); ++j) {
        if (i == j) continue;
        if (!validMutation(bank[i], bank[j])) continue;
        adjList[bank[i]].push_back(bank[j]);
        adjList[bank[j]].push_back(bank[i]);
      }
    }

    struct Compare{
      bool operator()(pair<string, int>& a, pair<string, int>& b) {
        return a.first > b.first;
      }
    };

    priority_queue<pair<string, int>, vector<pair<string, int>>, Compare> bfsq;
    unordered_map<string, bool> visited;
    bfsq.push({startGene, 0});
    
    while (!bfsq.empty()) {
      auto [curGene, dist] = bfsq.top();
      bfsq.pop();
      visited[curGene] = true;

      for (const auto& gene : adjList[curGene]) {
        if (gene == endGene) return dist + 1;
        if (visited[gene]) continue;
        bfsq.push({gene, dist + 1});
      }
    }

    return -1;
  }
};

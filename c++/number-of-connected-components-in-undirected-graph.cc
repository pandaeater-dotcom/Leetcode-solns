class Solution {
public:
  void exploreComp(unordered_map<int, vector<int>>& adjList, vector<bool>& visited, int node) {
    visited[node] = true;
    for (const auto& adj : adjList[node]) {
      if (visited[adj]) continue;
      exploreComp(adjList, visited, adj);
    }
  }

  int countComponents(int n, vector<vector<int>>& edges) {
    unordered_map<int, vector<int>> adjList;
    vector<bool> visited(n, false);

    for (int i = 0; i < n; ++i) {
      adjList[i].clear();
    }

    for (const auto& edge : edges) {
      adjList[edge[0]].push_back(edge[1]);
      adjList[edge[1]].push_back(edge[0]);
    }
    
    int treeCount = 0;

    for (const auto& [vertex, adjs] : adjList) {
      if (visited[vertex]) continue;
      cout << vertex << endl;
      exploreComp(adjList, visited, vertex);
      treeCount++;
    }

    return treeCount;
  }
};

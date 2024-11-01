class Solution {
public:
    string alienOrder(vector<string>& words) {
      int n = words.size();
      
      unordered_map<char,vector<char>> graph;
      unordered_map<char,int> indegree;

      for (auto& word : words)
        for (char c : word)
            indegree[c] = 0;
      
      for(int i = 0; i < n - 1; i++){
        string word1 = words[i];
        string word2 = words[i + 1];
        bool found = false;
        
        for (int j = 0; j < min(word1.size(), word2.size()); j++){
          if (word1[j] == word2[j]) continue;
          graph[word1[j]].push_back(word2[j]);
          indegree[word2[j]]++;
          found = true;
          break;
        }

        if (!found && word1.size() > word2.size()) return "";

        if(!found && word1.size() < word2.size()) {
          graph[word1.back()].push_back(word2[word1.size()]);
          indegree[word2[word1.size()]]++;
        }
      }
      
      queue<char> q;
      string ans = "";
      for (auto& entry : indegree){
        char node = entry.first;
        if (entry.second == 0)
            q.push(node);
      }

      while(!q.empty()){
        char node = q.front();
        q.pop();
        ans += node;
        for(char nbr : graph[node]){
          if(!--indegree[nbr]) q.push(nbr);
        }
      }

      if(ans.size() != indegree.size()) return "";
      return ans;
  }
};

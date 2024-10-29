class Solution {
public:
  vector<int> assignTasks(vector<int>& servers, vector<int>& tasks) {
    struct Compare {
      bool operator()(pair<int, int>& a, pair<int, int>& b) {
        if (a.first == b.first) return a.second > b.second;
        return a.first > b.first;
      }
    };

    priority_queue<pair<int, int>, vector<pair<int, int>>, Compare> free, busy;
    vector<int> assign;
    string a = "";
    int time = 0;

    for (int i = 0; i < servers.size(); ++i) {
      free.push({servers[i], i});
    }

    int i = 0;
    for (; i < tasks.size(); ++i) {
      int time = max(time, i);

      if (free.empty()) {
        time = busy.top().first;
      }
      while (!busy.empty() && busy.top().first <= time) {
        auto p = busy.top();
        busy.pop();
        free.push({servers[p.second], p.second});
      }

      auto [weight, index] = free.top();
      free.pop();
      busy.push({time + tasks[i], index});
      assign.push_back(index);
    }

    for (int num : assign) {
      cout << num << " ";
    }

    return assign;
  }
}

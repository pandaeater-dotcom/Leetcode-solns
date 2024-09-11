class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> adjList(numCourses, vector<int>());
        vector<int> courseOrder;
        vector<int> status(numCourses, 0);
        
        for (const auto& it : prerequisites) {
            adjList[it[1]].push_back(it[0]);
        }

        for (int pre = 0; pre < numCourses; ++pre) {
            if (status[pre]) continue;
            if (!recursiveDfs(adjList, courseOrder, status, pre)) return {};
        }

        reverse(courseOrder.begin(), courseOrder.end());
        return courseOrder;
    }

    bool recursiveDfs(vector<vector<int>>& adjList, vector<int>& courseOrder, vector<int>& status, int pre) {
        if (status[pre] == 2) return true;
        else if (status[pre] == 1) return false;

        status[pre] = 1;
        for (auto& neighbour : adjList[pre]) {
            if (!recursiveDfs(adjList, courseOrder, status, neighbour)) return false;
        }
        status[pre] = 2;
        courseOrder.push_back(pre);
        return true;
    }
};
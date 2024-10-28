class Vector2D {
private:
  int index;
  int subIndex;
  vector<vector<int>>& vec;
public:
  Vector2D(vector<vector<int>>& vec): index{-1}, subIndex{-1}, vec{vec} {
    if (!hasNext()) return;
    index = 0;
    subIndex = 0;
    while (index < vec.size() && vec[index].empty()) {
      index++;
    }
  }
  
  int next() {
    if (subIndex < vec[index].size()) {
      return vec[index][subIndex++];
    }
    subIndex = 0;
    index++;
    while (index < vec.size() && vec[index].empty()) {
      index++;
    }
    return vec[index][subIndex++];
  }
  
  bool hasNext() {
    int tempIndex = index == -1 ? 0 : index;
    int tempSubIndex = index == -1 ? 0 : subIndex;

    for (; tempIndex < vec.size(); ++tempIndex) {
      if (tempSubIndex >= vec[tempIndex].size()) {
        tempSubIndex = 0;
        continue;
      }
      return true;
    }
    return false;
  }
};

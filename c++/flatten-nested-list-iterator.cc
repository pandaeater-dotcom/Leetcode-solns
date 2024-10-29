class NestedIterator {
private:
  vector<int> flat;
  int nextInt;

  void flatten(const vector<NestedInteger> &nestedList) {
    for (const auto& ni : nestedList) {
      if (ni.isInteger()) {
        flat.push_back(ni.getInteger());
      } else {
        flatten(ni.getList());
      }
    }
  }
public:
  NestedIterator(vector<NestedInteger> &nestedList): nextInt{0} {
    flatten(nestedList);
  }
  
  int next() {
    return flat[nextInt++];
  }
  
  bool hasNext() {
    return nextInt < flat.size();
  }
}

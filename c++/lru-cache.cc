class LRUCache {
private:
  int capacity;
  list<pair<int, int>> active;
  unordered_map<int, list<pair<int, int>>::iterator> cache;

  void moveToFront(int key) {
    active.splice(active.begin(), active, cache[key]);
    cache[key] = active.begin();
  }

public:
  LRUCache(int capacity): capacity{capacity} {}
  
  int get(int key) {
    if (!cache.contains(key)) return -1;
    moveToFront(key);

    return cache[key]->second;
  }
  
  void put(int key, int value) {
    bool exists = cache.contains(key);
    if (exists) {
      moveToFront(key);
      active.front().second = value;
      return;
    }
    if (active.size() >= capacity) {
      cache.erase(active.back().first);
      active.pop_back();
    }
    active.push_front({key, value});
    cache[key] = active.begin();
  }
};

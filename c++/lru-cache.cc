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
    LRUCache(int capacity): capacity{capacity} {
    }
    
    int get(int key) {
        if (!cache.contains(key)) return -1;
        moveToFront(key);

        return cache[key]->second;
    }
    
    void put(int key, int value) {
        bool exists = cache.contains(key);
        if (active.size() >= capacity && !exists) {
            auto it = active.back();
            active.pop_back();
            cache.erase(it.first);
        }
        if (!exists) {
            active.emplace_front(key, value);
            cache[key] = active.begin();
            return;
        }
        moveToFront(key);
        cache[key]->second = value;
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
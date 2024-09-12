class RandomizedSet {
private:
    vector<int> elements;
    unordered_map<int, int> position; // 1-indexed
public:
    RandomizedSet() {
    }
    
    bool insert(int val) {
        cout << position[val] << endl;
        if (position[val]) return false;
        elements.push_back(val);
        position[val] = elements.size();
        return true;
    }
    
    bool remove(int val) {
        if (!position[val]) return false;
        int index = position[val] - 1;
        elements[index] = elements[elements.size() - 1];
        position[elements[index]] = index + 1;
        position[val] = 0;
        elements.pop_back();
        return true;
    }
    
    int getRandom() {
        int index = rand()%elements.size();
        return elements[index];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */
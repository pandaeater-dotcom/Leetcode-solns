class Solution {
public:

    void fixup(vector<pair<int, int>>& heap, int i) {
        int parent_index = floor((i - 1)/2);
        while (parent_index >= 0 && heap[parent_index].second < heap[i].second)
        {
            swap(heap[parent_index], heap[i]);
            i = parent_index;
            parent_index = floor((i - 1)/2);
        }
    }

    void fixdown(vector<pair<int, int>>& heap, int i) {
        int len = heap.size() - 1;
        while (2*i + 1 <= len)
        {
            int child = 2*i + 1;
            if (len > child && heap[child].second < heap[child + 1].second)
                child++;
            if (heap[i].second >= heap[child].second)
                break;
            swap(heap[i], heap[child]);
            i = child;
        }
    }

    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> frequency_map;
        vector<pair<int, int>> frequency_heap;
        vector<int> most_frequent;


        for (const auto& num : nums)
            frequency_map[num]++;
        for (const auto& it : frequency_map)
        {
            frequency_heap.push_back(it);
            fixup(frequency_heap, frequency_heap.size() - 1);
        }
        for (const auto& it : frequency_heap)
        {
            cout << it.first << " " << it.second << endl;
        }
        for (int i = 0; i < k; i++)
        {
            most_frequent.push_back(frequency_heap[0].first);
            swap(frequency_heap[0], frequency_heap[frequency_heap.size() - 1]);
            frequency_heap.pop_back();
            fixdown(frequency_heap, 0);
        }

        return most_frequent;
    }
};

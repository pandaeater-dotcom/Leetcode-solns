class LogSystem {
private:
  unordered_map<int, set<string>> logs;
public:
  LogSystem() {}
  
  void put(int id, string timestamp) {
    logs[id].insert(timestamp);
  }

  int getGran(string granularity) {
    if (granularity == "Year") return 4;
    if (granularity == "Month") return 7;
    if (granularity == "Day") return 10;
    if (granularity == "Hour") return 13;
    if (granularity == "Minute") return 16;
    if (granularity == "Second") return 19;
    return 19;
  }
  
  vector<int> retrieve(string start, string end, string granularity) {
    vector<int> relevantLogs;
    int gran = getGran(granularity);

    string prefix_start = start.substr(0, gran);
    string prefix_end = end.substr(0, gran);

    for (const auto& [id, times] : logs) {
      for (const auto& ts : times) {
        string prefix_ts = ts.substr(0, gran);
        if (prefix_ts < prefix_start || prefix_ts > prefix_end) continue;
        relevantLogs.push_back(id);
      }
    }

    return relevantLogs;
  }
};

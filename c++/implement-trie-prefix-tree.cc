class Trie {
private:
  vector<Trie*> children;
  bool isWord;
  string str;
public:
  Trie(): isWord{false}, str{""} {}

  Trie(char ch): str{ch}, isWord{false} {}
  
  void insert(string word) {
    if (word == "") {
      isWord = true;
      return;
    }
    for (auto& child : children) {
      string res = child->getChar();
      if (res.length() && res[0] == word[0]) {
        child->insert(word.substr(1));
        return;
      }
    }
    children.push_back(new Trie(word[0]));
    children.back()->insert(word.substr(1));
  }
  
  bool search(string word) {
    
    if (word == "") {
      if (isWord) return true;
      return false;
    }
    for (const auto& child : children) {
      string res = child->getChar();
      if (res.length() && res[0] == word[0]) {
        return child->search(word.substr(1));
      }
    }
    return false;
  }
  
  bool startsWith(string prefix) {
    if (prefix == "") return true;
    for (const auto& child : children) {
      string res = child->getChar();
      if (res.length() && res[0] == prefix[0]) {
        return child->startsWith(prefix.substr(1));
      }
    }
    return false;
  }

  string getChar() {
    return str;
  }
};

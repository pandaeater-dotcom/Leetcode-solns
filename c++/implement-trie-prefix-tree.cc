class Trie {
private:
  array<Trie*, 26> children;
  bool isWord;
public:
  Trie(): isWord{false} {
    children.fill(nullptr);
  }
  
  void insert(string word) {
    if (word == "") {
      isWord = true;
      return;
    }
    int index = word[0] - 'a';
    if (!children[index]) children[index] = new Trie();
    children[index]->insert(word.substr(1));
  }
  
  bool search(string word) {
    if (word == "") {
      if (isWord) return true;
      return false;
    }
    int index = word[0] - 'a';
    if (!children[index]) return false;
    return children[index]->search(word.substr(1));
  }
  
  bool startsWith(string prefix) {
    if (prefix == "") return true;
    int index = prefix[0] - 'a';
    if (!children[index]) return false;
    return children[index]->startsWith(prefix.substr(1));
  }
};

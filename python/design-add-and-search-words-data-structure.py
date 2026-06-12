class WordDictionary:

    class Trie:
        def __init__(self, letter):
            self.letter = letter
            self.children = {}
    def __init__(self):
        self.trie = self.Trie('.')

    def addWord(self, word: str) -> None:
        trie = self.trie
        if not word:
            return
        index = 0
        while index < len(word):
            ch = word[index]
            if ch in trie.children:
                trie = trie.children[ch]
            else:
                newTrie = self.Trie(ch)
                trie.children[ch] = newTrie
                trie = newTrie
            index += 1
        trie.children['.'] = self.Trie('.')

    def search(self, word: str) -> bool:
        def recursiveSearch(trie = self.trie, index = 0):
            if index >= len(word):
                return '.' in trie.children
            if word[index] == '.':
                return any([recursiveSearch(child, index + 1) for child in trie.children.values()])
            if word[index] in trie.children:
                return recursiveSearch(trie.children[word[index]], index + 1)
            return False
        return recursiveSearch()


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

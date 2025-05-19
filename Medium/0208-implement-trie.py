class TrieNode:
    def __init__(self):
        self.children = {} # Key: character, value: TrieNode
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode() # Create new TrieNode

            curr = curr.children[c]

        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root 

        for c in word:
            if c not in curr.children:
                return False

            curr = curr.children[c]
        
        return curr.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root 

        for c in prefix:
            if c not in curr.children:
                return False

            curr = curr.children[c]
        
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

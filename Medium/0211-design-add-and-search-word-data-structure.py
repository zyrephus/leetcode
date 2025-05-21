class TrieNode:
    def __init__(self):
        self.children = {} # Character: TrieNode
        self.is_end_of_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()

            curr = curr.children[c]
        
        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(node: TrieNode, i: int) -> bool:
            if i == len(word):
                return node.is_end_of_word
            
            c = word[i]
            # Try all possible children for "."
            if c == ".":
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False

            else:
                if c not in node.children:
                    return False
                return dfs(node.children[c], i + 1)

        return dfs(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

class TrieNode:
        def __init__(self):
            self.children = {} # Character: TrieNode
            self.is_word = False
        
        def addWord(self, word):
            curr = self

            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            
            curr.is_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            root.addWord(word)
        
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(row, col, node, word):
            if (row < 0 or col < 0 or
                row == ROWS or col == COLS or
                (row, col) in visit or
                board[row][col] not in node.children):
                return

            visit.add((row, col))

            node = node.children[board[row][col]]
            word += board[row][col]
            if node.is_word:
                res.add(word)

            dfs(row + 1, col, node, word)
            dfs(row - 1, col, node, word)
            dfs(row, col + 1, node, word)
            dfs(row, col - 1, node, word)

            visit.remove((row, col))

        for row in range(ROWS):
            for col in range(COLS):
                dfs(row, col, root, "")

        return list(res)

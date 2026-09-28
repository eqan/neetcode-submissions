class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        '''
            Developing a Tree first for search optimization
        '''
        def add(root, word):
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.word = True
        for word in words:
            add(root, word)
        '''
            Searching each character of the grid for the word via DFS and Backtracking
        '''
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()
        def dfs(r, c, node, word):
            # Edge case for grid
            if (r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visit or board[r][c] not in node.children):
                return
            # Adding to visit
            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            # If we found the word then we add
            if node.word:
                res.add(word)
            dfs(r-1,c,node,word)
            dfs(r+1,c,node,word)
            dfs(r,c-1,node,word)
            dfs(r,c+1,node,word)
            # After finishing the visits we backtrack
            visit.remove((r,c))
        # DFS on each every character
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        return list(res)
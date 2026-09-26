class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    '''
        Typical Trie implementation for add word
    '''
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True
        

    '''
        This has to be modified as we have to backtrack to reach desired element
    '''
    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root # Using the current reached node as root
            for i in range(j, len(word)): # Using j to resume where we left off in the backtrack
                c = word[i]
                if c == '.': # We found '.' then we try to iterate all values of the current nodes children and perform DFS on them
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False # After even going through DFS on all the nodes then we can assume we didnt find any relevant node
                else: # Same case as a trie node if we didnt find it return False
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.word
        return dfs(0, self.root)
        

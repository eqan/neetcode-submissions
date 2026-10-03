class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        par = [i for i in range(N+1)] # ith node -> parent (i - n) Exaplanation for +1 given below
        rank = [1] * (N + 1) # Initalising 1 for all nodes in the list (+1 because as you know we add a 1 to complete the number of nodes from count of edges)

        def find(n):
            if n != par[n]:
                par[n] = find(par[n]) # Path Compression
            return par[n]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False # if the parents are matching then we have found a cycle
            
            if rank[p1] > rank[p2]: # if rank of p1 is greater than rank of p2 then that means p2 needs to be merged into p1 Tree
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

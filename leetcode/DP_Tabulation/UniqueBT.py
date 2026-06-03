class Solution:
    def numTrees(self, n: int) -> int:
        new_tree = [1] * (n + 1)
        
        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                total += new_tree[root - 1] * new_tree[nodes - root]
            new_tree[nodes] = total
        
        return new_tree[n]
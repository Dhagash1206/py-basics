class Solution:
    def allPossibleFBT(self, n: int):

        if n % 2 == 0:
            return []

        dp = []

        for i in range(n + 1):
            dp.append([])

        dp[1] = [TreeNode(0)]

        def func(nodes):

            if dp[nodes]:
                return dp[nodes]

            trees = []

            for l in range(1, nodes, 2):

                r = nodes - 1 - l

                left_trees = func(l)
                right_trees = func(r)

                for left_tree in left_trees:
                    for right_tree in right_trees:

                        root = TreeNode(0)

                        root.left = left_tree
                        root.right = right_tree

                        trees.append(root)

            dp[nodes] = trees

            return trees

        return func(n)
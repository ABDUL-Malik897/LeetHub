class Solution(object):

    def maxProduct(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        MOD = 10**9 + 7

        # Step 1: Find total sum of the tree
        total = 0
        stack = [root]

        while stack:
            node = stack.pop()

            if node:
                total += node.val
                stack.append(node.left)
                stack.append(node.right)

        # Step 2: Postorder traversal to calculate subtree sums
        maximum = 0
        stack = [(root, False)]
        subtree_sum = {}

        while stack:
            node, visited = stack.pop()

            if not node:
                continue

            if visited:
                left_sum = subtree_sum.get(node.left, 0)
                right_sum = subtree_sum.get(node.right, 0)

                current_sum = node.val + left_sum + right_sum
                subtree_sum[node] = current_sum

                product = current_sum * (total - current_sum)
                maximum = max(maximum, product)

            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))

        return maximum % MOD
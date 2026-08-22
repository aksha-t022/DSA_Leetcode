class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        def h(root):
            if root == None: return 0
            lh = h(root.left)
            rh = h(root.right)
            ans[0] = max(ans[0], lh+rh)
            return max(lh, rh) + 1
            
        h(root)
        return ans[0]
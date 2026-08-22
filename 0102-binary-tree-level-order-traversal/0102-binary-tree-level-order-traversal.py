# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []
        tempAns = []
        dq = deque([root, None])
        while dq:
            temp = dq.popleft()

            if temp is None:
                ans.append(tempAns[:]) 
                tempAns.clear()
                if dq:
                    dq.append(None)
            else:
                tempAns.append(temp.val)
                if temp.left:
                    dq.append(temp.left)
                if temp.right:
                    dq.append(temp.right)
        return ans
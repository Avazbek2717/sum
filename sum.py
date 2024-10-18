# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, curSum):
            if not node:
                return False
            curSum = curSum + node.val
            if not node.left and not node.right:
                return curSum == targetSum
            
            return dfs(node.left, curSum) or dfs(node.right, curSum)
        
        return dfs(root, 0)


            


# root = TreeNode(5)
# root.left = TreeNode(4)
# root.right = TreeNode(8)
# root.left.left = TreeNode(11)
# root.left.left.left = TreeNode(7)
# root.left.left.right = TreeNode(2)
# root.right.left = TreeNode(13)
# root.right.right = TreeNode(4)
# root.right.right.right = TreeNode(1)
# targetSum  = 22


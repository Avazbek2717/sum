# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
#         def dfs(node, curSum):
#             if not node:
#                 return False
#             curSum = curSum + node.val
#             if not node.left and not node.right:
#                 return curSum == targetSum
            
#             return dfs(node.left, curSum) or dfs(node.right, curSum)
        
#         return dfs(root, 0)


            


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




#118- misol

# def palindrom( numRows: int):
#     t = [[1]]
#     for i in range(numRows-1):
#         tempt = [0] + t[-1] +[0]
#         row = []
#         for j in range(len(t[-1])+1):
#             row.append(tempt[j]+tempt[j+1])
#         t.append(row)
#     return  t

# print(palindrom(10))


# # 58 - misol
# a = 'Hello world'
# b = a.split()
# v = len(b[-1])

# c = pow(2,31)
# print(c)




# 202 - misol


# def get(n):

#     s = set()  
#     while n != 1 and n not in s:
#         s.add(n)  
#         nsum = 0
#         while n>0:
#             n,digit = divmod(n,10)
#             nsum+=digit**2
#         n = nsum
#     return n==1


# print(get(19))


def get(n):
            s = set()
            while n!=1 and n not in s:
                s.add(n)
                nsum = 0
                while n>0:
                    n,digit = divmod(n,10)
                    nsum = nsum + digit**2
                n = nsum
            return n == 1

print(get(19))






















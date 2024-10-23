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
#             s = set()
#             while n!=1 and n not in s:
#                 s.add(n)
#                 nsum = 0
#                 while n>0:
#                     n,digit = divmod(n,10)
#                     nsum = nsum + digit**2
#                 n = nsum
#             return n == 1

# print(get(19))



# 52 - misol

# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         v = x**n
#         return v



# '''Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.'''

# def twosum(a: list, b:list):


  

    
#     c = ''.join(map(str,a))
#     v = ''.join(map(str,b))
#     g = int(c) + int(v)
#     h = [int(digit) for digit in str(g)]
#     o = h[::-+1]

#     return o 

# print(twosum([2,4,3],[5,6,4]))





   # if a == [0] and b == [0]:
    #     return [0]


#     v = (lambda d,f: d+f)
#     c = list(map(v,a,b))
#     return c

# print(twosum((1,2),(1,2)))





# def eng_katt_son(a: int):
#     raqamlar = list(str(a))
#     raqamlar.sort(reverse=True)
#     return int(''.join(raqamlar))

# print(eng_katt_son(12345))


'''eng katta sonni topish'''
# def eng_katta_son(a:int):
#     raqmalar = list(str(a))
#     for i in range(len(raqmalar)):
#         for j in range(i+1,len(raqmalar)):
#             if raqmalar[i]<raqmalar[j]:
#                 raqmalar[i],raqmalar[j] = raqmalar[j],raqmalar[i]
#     return int(''.join(raqmalar))

# print(eng_katta_son(546))

    
# def maximum69Number (self, num: int) -> int:
#     n = str(num)
#     m_n = num
#     for i in range(len(n)):
#         new_str = n[:i] + '9'+ n[i+1]
#         new = str(new_str)
#     if new > m_n:
#         m_n = new
#     return m_n


# print(maximum69Number(69))
        








# def get(n):
#             s = set()
#             while n!=1 and n not in s:
#                 s.add(n)
#                 nsum = 0
#                 while n>0:
#                     n,digit = divmod(n,10)
#                     nsum = nsum + digit**2
#                 n = nsum
#             return n == 1

# print(get(1111111))





def strStr( haystack: str, needle: str):
    l1 = len(haystack)
    l2 = len(needle)
    for i in range(l1-l2+1):
        if haystack[i:i+l2] == needle:
            return i
    return -1

haystack = "sadbutsad"
needle = "sad"
b = strStr(haystack,needle)
print(b)
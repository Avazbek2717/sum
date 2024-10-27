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





# def strStr( haystack: str, needle: str):
#     l1 = len(haystack)
#     l2 = len(needle)
#     for i in range(l1-l2+1):
#         if haystack[i:i+l2] == needle:
#             return i
#     return -1

# # haystack = "sadbutsad"
# # needle = "sad"
# b = strStr('hello','ll')
# print(b)




'''Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:'''

# def threesum(a:list):
#     a.sort()
#     result  = []
#     c = len(a)
#     for i in range(c-2):
#         if i >0 and a[i]==a[i-1]:
#             continue
#         for j in range(i+1,c-1):
#             if j>i+1 and a[j] == a[j-1]:
#                 continue
#             for k in range(j+1,c):
#                 if k>j+1 and a[k]==a[k-1]:
#                     continue
#                 if a[i]+a[j]+a[k] ==0:
#                     result.append([a[i],a[j],a[k]])
#     return result

# print(threesum([0,1,1]))

# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         n_str =''.join(map(str,digits))
#         q_n =int(n_str)+1
#         l = [int (digit) for digit in str(q_n) ]
#         return l
            

'''Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores)'''
# def get_dubl(nums: list):
#     c = 1
#     b = []
#     for i in range(1,len(nums)):
#         if nums[i] != nums[i-1]:
#             nums[c] = nums[i]
#             b.append(nums[c])
#     return b

# print(get_dubl([1,1,2]))

# a = [1,1,2]
# b = lambda c: 
# def remove_duplicates(lst):
#     result = []
#     seen = set()
    
#     for item in lst:
#         if item in seen:
#             result.append('_')
#         else:
#             result.append(item)
#             seen.add(item)
    
#     return result

# # Misol ro'yxat
# input_list = [1, 1, 2]
# output_list = remove_duplicates(input_list)
# print(output_list)





# def intt(x: int):
#     b = str(x)
#     c = list(b[::-1])
#     c.pop(0)
#     c.insert(0,'-')
#     p = str(c)

#     return int(p)

# print(intt(-12))

# class Solution:
#     def reverse(self, x: int) -> int:


#         if x < 0:
#             r = -int(str(abs(x))[::-1])
#         else:
#             r = int(str(x)[::-1])
        


#         if r not in range(-2**31, 2**31-1):
#             return 0
#         return r





# def get_dubl(nums: list):
#     c = 1
#     b = []
#     for i in range(1,len(nums)):
#         if nums[i] != nums[i-1]:
#             nums[c] = nums[i]
#             b.append(nums[c])
#     return b

# print(get_dubl([1,1,2]))


# def remove(nums):
#     l = 1
#     for i in range(1,len(nums)):
#         if nums[i]!=nums[i-1]:
#             nums[l] = nums[i]
#             l+=1
#     return l

# print(remove([1,1,2]))


def ugly_number(n):
    if n<=0:
        return False
    
    for i in [2,3]:
        if n<=0:
            return False
        while n%i==0:
            n = n//i
            return False
    return n==1

print(ugly_number(0))
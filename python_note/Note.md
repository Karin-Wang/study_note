# Karin's Algorithm Note ^^

- sort object by attribute:
`obj.sort(key = lambda x:x.atribute, reverse = True/False)`

- sort dictionary by value in decreasing order:
`sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)`

### Linked List 

- Find middle point in a linked list(in the format of node class)
```
# slow step: 1 ; fast step : 2
slow, fast = head, head.next.next
while fast and fast.next:
    fast = fast.next.next
    slow = slow.next
# mid: points to root
mid = slow.next
```

- [Floyd's cycle detection algorithm a.k.a hare and tortoise algorithm:](https://www.geeksforgeeks.org/find-duplicates-in-on-time-and-constant-extra-space/)
**Basic thought:**

**2 pointer, one slow, one fast**

如果没有cycle， 则slow和fast只可能在终点相遇

如果与cycle, 则slow和fast都在环里绕圈，slow会被fast套圈追上

```
def hasCycle(self, head):
    try:
        slow = head
        fast = head.next
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
        return True
    except:
        return False
```

- replace and add something in original string
```
''.join(s.replace('|', '||') + ' | ' for s in strs)
```

- deal with duplicate elements in rotated sorted list(part in binary search)
```
        while l < mid and nums[l] == nums[mid]: # tricky part DiaoDiaoDiao aaaaa
            l += 1
```

### Bit Manipulation

- Bitwise Operators

Operator| Description | Example 
--------|-------------|--------
`&`     | Copies a bit to the result if it exists in both operands | **2 & 1** equals to **10 & 01** = 00 <br> **3 & 1** equals to **11 & 01** = 01   
`\|`     | Copies a bit to the result if it exists in either operands | **2 \| 1** equals to **10 \| 01** = 11 <br> **3 \| 1** equals to **11 \| 01** = 11   
`^`     | Copies a bit to the result if there is a 0 in one and 1 in the other| **2 & 1** equals to **10 & 01** = 11 <br> **3 & 1** equals to **11 & 01** = 10   
`x>>C`    | x shift to right in C steps(cut right C bits) | **1011 >> 2** = **10**
`x<<C`    | x shift to left in C steps(add C of 0 to the right) | **1011 << 2** = **101100**

- Bit Manipulation
**Sum of 2 Inegers without using any arithmetic operators**
```
def Add(x, y):
 
    # Iterate till there is no carry 
    while (y != 0):
     
        # carry now contains common
        # set bits of x and y
        carry = x & y
 
        # Sum of bits of x and y where at
        # least one of the bits is not set
        x = x ^ y
 
        # Carry is shifted by one so that   
        # adding it to x gives the required sum
        y = carry << 1
     
    return x
```

### Sort

- Insertion Sort

- Merge Sort

- Quick Sort

- Bucket Sort

- Sort only using Stack

### Linked List
- Reverse Linked List
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev
```

### Tree 

**Traversal**:

- Pre-Order 中左右

Usage: 

1. create a copy of the tree

2. get prefix expression on of an expression tree 

3. DFS traversal of tree


```
def preOrder(root):
    stack,res = [root],[]
    while stack:
        root = stack.pop()
        if root:
            res.append(root.val)
            stack.append(root.right)
            stack.append(root.left)
    return res
            
```

- In-Order 左中右

Usage: `non-decreasing order`

```
def inOrder(root):
    stack, res = [],[]
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        res.append(root.val)
        root = root.right
    return res
```

- Post-Order 左右中

The reverse of pre-order

Usage: delete the tree

1: Real post order, using a flag to indicate whether the node has been visited or not.
```
class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def postorderTraversal(self, root):
        traversal, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    # add to result if visited
                    traversal.append(node.val)
                else:
                    # post-order
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))

        return traversal
```

2: pre-order edition(right subtree first)
```
def postOrder(root):
    stack, res = [root],[]
    while stack:
        root = stack.pop()
        if root:
            res.append(root.val)
            stack.append(root.left)
            stack.append(root.right)
    return res[::-1]    # reverse
```

- Level-Order
```
def level-order(root):
    if not root: return []
    res,level = [],[root]
    while level:
        res.append([node.val for node in level])
        temp = []
        for node in level:
            temp += [node.left,node.right] 
        level = [leaf for leaf in temp if leaf]
    return res
```


**Some Trees**

- Trie
```
class Trie:
    def __init__(self):
        self.tree = {}
        
    def insert(self,word):
        tree = self.tree
        for char in word:
            if char not in tree:
                tree[char] = {}
            tree = tree[char]
        tree['exist'] = True
        
    def search(self, word):
        tree = self.tree
        for char in word:
            if char not in tree:
                return False
            tree = tree[char]
        return ('exist' in tree and tree['exist'] == True)
    
    def findPrefix(self,prefix):
        tree = self.tree
        for char in prefix:
            if char not in tree:
                return False
            tree = tree[char]
        return True
```
- BST

- Difference from Binary Heap

### Graph

**Traversal**

- DFS

 [200. Number of Islands](https://leetcode.com/problems/number-of-islands/description/)
 
 [417. Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/description/)
 
 [114. Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/)
 

- BFS
```

```

**Algorithm**

- Dijkstra

- Topological Sort
```
        connections = {i:[] for i in range(numCourses)}
        indegrees = [0 for _ in range(numCourses)]
        for p in prerequisites:
            connections[p[1]].append(p[0])
            indegrees[p[0]]+=1
        zeroDegrees = [index for index, value in enumerate(indegrees) if value==0]
        count = 0
        while len(zeroDegrees) > 0:
            count += 1
            for node in connections[zeroDegrees.pop()]:
                indegrees[node] -= 1
                if indegrees[node] == 0:
                    zeroDegrees.append(node)
        return (count == numCourses)
```

- Union Find

https://github.com/XinyueWang94/study_note/blob/master/python_note/Union_Find.py



### Dynamic Programming

- Fibonacci 
```
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a,b = 1,1
        for _ in range(n-1):
            a,b = b,a+b
        return a
```


### BackTracking

- Backtracking
```
class Subset: 
    def subsets(self, S):
        self.result = []
        self.backtrack(0, sorted(S), [])
        return self.result

        # general template
    def backtrack(self, start, S, temp):
        self.result.append(temp[:])
        for i in range(start , len(S)):
            temp.append(S[i])
            self.backtrack(i + 1, S, temp)
            temp.pop()
```

### Union Find

```
class QuickFind:
    def __init__(self):
        self.id = {}
            
    def connected(self,p,q):
        return self.find(p) == self.find(q)
    
    def find(self,p):  
        if p not in self.id:
            self.id[p] = p
        while p in self.id and self.id[p] != p:
            p = self.id[p]
        return self.id[p]
    
    def union(self,p,q):
        p = self.find(p)
        q = self.find(q)
        self.id[p] = q
```

### Quick Selection

**Kth Largest Element in an Array**

```
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.find(nums, k)
        
    def partition(self, start, end, nums):
        high = start
        while start < end:
            if nums[start] > nums[end]:
                nums[start], nums[high] = nums[high], nums[start]
                high += 1
            start += 1
        nums[end], nums[high] = nums[high], nums[end]
        return high
        
        
    def find(self, nums, k):
        pos = self.partition(0, len(nums)-1, nums)
        if pos + 1 == k:
            return nums[pos]
        elif pos + 1 > k:
            return self.find(nums[:pos], k)
        else:
            return self.find(nums[pos+1:], k - pos - 1)
```

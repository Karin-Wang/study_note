# Python Note

- sort object by attribute:
`obj.sort(key = lambda x:x.atribute, reverse = True/False)`

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

- Backtracking
```
class Subset: 
    def subsets(self, S):
        self.result = []
        self.backtrack(0, sorted(S), [])
        return self.result

        # general idea
    def backtrack(self, start, S, temp):
        self.result.append(temp[:])
        for i in range(start , len(S)):
            temp.append(S[i])
            self.backtrack(i + 1, S, temp)
            temp.pop()
```

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

### Sort

- Insertion Sort

- Merge Sort

- Quick Sort

- Bucket Sort

- Sort only using Stack

### Tree 

**Traversal**:

- Pre-Order

- In-Order

- Post-Order

- Level-Order

**Some Trees**

- Trie

- BST

- Difference from Binary Heap

### Graph

**Traversal**

- DFS

- BFS

**Algorithm**

- Dijkstra

- Topological Sort

- Union Find


### Dynamic Programming


### BackTracking




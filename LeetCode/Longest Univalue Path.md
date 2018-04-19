# Longest Univalue Path

## Problem
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.

Input1:
```
              5
             / \
            4   5
           / \   \
          1   1   5
```

Result1: 

```
2
```


Input2:
```
              1
             / \
            4   5
           / \   \
          4   4   5
```

Result2: 

```
2
```


## Solution

My initial intuition is pre-order but found it's impossible, cuz in that case we can only record the longest path either in the left
tree or right tree, but cannot combine them together in a good way.

The correct idea is to do it in DFS traverse. Similar to `Diameter of Binary Tree`. The point is to keep track of the `longest` as well as record the local longest path under
each subroot.

To record the `longest`, we use :

```
self.longest = max(self.longest, left + right)
```

For left and right under each parent, if not 0 then it means they have the same value, thus we can sum them up and compare to the 
class variable `longest`.

However as regards to the return value in each `traverse` it is needed to record the longest path in either left or right tree plus one if 
the node has the same value as it's parent.

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.longest = 0
        def traverse(node, parent_val):
            if not node:
                return 0
            left, right = traverse(node.left, node.val), traverse(node.right, node.val)
            self.longest = max(self.longest, left + right)
            return 1 + max(left, right) if node.val == parent_val else 0
        traverse(root, None)
        return self.longest
```

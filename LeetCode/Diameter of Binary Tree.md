# Problem
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:

Given a binary tree 
```
          1
         / \
        2   3
       / \     
      4   5    
```

Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.

# Solution

It's a problem similar to [Longest Univalue Path](https://github.com/XinyueWang94/study_note/blob/master/LeetCode/Longest%20Univalue%20Path.md)
, but without any extra condition. 

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.longest = 0
        def traverse(root):
            if not root:  # if None then it's 0
                return 0
            l = traverse(root.left)
            r = traverse(root.right)
            self.longest = max(self.longest,l+r)
            return max(l,r)+1
        traverse(root)
        return self.longest
```

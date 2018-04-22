# Flip Game ||

## Problem
You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to determine if the starting player can guarantee a win.

For example, given s = "++++", return true. The starting player can guarantee a win by flipping the middle "++" to become "+--+".

Follow up:
Derive your algorithm's runtime complexity.


## Solution
`Backtracking`

### Without Memorization - 1052ms

`O(n!!)` - not sure
```
class Solution:
    def canWin(self, s):
        for i in range(len(s)-1):
            if s[i]=='+' and s[i+1]=='+' and not self.canWin(s[:i]+'--'+s[i+2:]): return True
        return False
```


### Optimization: With Memorization - 64ms

- **Use Dictionary to record the calculted bool value for string**

`O(n^2)` - not sure  [max number of substring of a string : n*(n-1)/2]

```
# With Memory
class Solution:
    def __init__(self):
        self.dict1 = {}
    def canWin(self, s):
        for i in range(len(s)-1):
            if s[i]=='+' and s[i+1]=='+':
                temp = s[:i]+'--'+s[i+2:]
                if temp in self.dict1: 
                    tempBool = self.dict1[temp]
                else:
                    tempBool = self.canWin(temp)
                    self.dict1[temp] = tempBool
                if not tempBool: 
                    return True
        return False
```

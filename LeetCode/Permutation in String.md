# Problem
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.


Example 1:

```
Input:s1 = "ab" s2 = "eidbaooo"
Output:True
Explanation: s2 contains one permutation of s1 ("ba").
```

Example 2:
```
Input:s1= "ab" s2 = "eidboaoo"
Output: False
```

## Note:
- The input strings only contain lower case letters.
- The length of both given strings is in range [1, 10,000].


# Solution
Sliding window.

For each window representing a substring of s2 of length len(s1), 
we want to check if the count of the window is equal to the count of s1. 
Here, the count of a string is the list of: [the number of a's it has, the number of b's,… , the number of z's.]

We can maintain the window by deleting the value of 
s2[i - len(s1)] when it gets larger than len(s1). 
After, we only need to check if it is equal to the target. 
Working with list values of [0, 1,…, 25] instead of ‘a’-‘z’ makes it easier to count later.


```
class Solution(object):
    def checkInclusion(self, s1, s2):
        A = [ord(x) - ord('a') for x in s1]   #alphabet distance to "a" ord ('a') = 97
        B = [ord(x) - ord('a') for x in s2]
        # print A
        print B

        target = [0] * 26
        for x in A:
            target[x] += 1
        # print target

        window = [0] * 26
        for i, x in enumerate(B):
            window[x] += 1
            print window
            print i
            if i >= len(A):
                window[B[i - len(A)]] -= 1 #window 右移,去掉最左边的在window中对应的
            if window == target:
                print target
                print window
                return True
        return False
```

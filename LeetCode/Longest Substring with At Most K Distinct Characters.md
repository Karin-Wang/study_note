# Problem
Given a string, find the length of the longest substring T that contains at most k distinct characters.

For example, Given s = “eceba” and k = 2,

T is "ece" which its length is 3.


# Solution
```
class Solution(object):
    
    """
    Time Complexity: O(n)
    Space Complexity: 
    "low": 当前substring在原string中的最左index
    The general idea is to iterate over string s.
    Always put the character c and its location i in the dictionary d.
    1) If the sliding window contains less than or equal to k distinct characters, simply record the return value, and move on.
    2) Otherwise, we need to remove a character from the sliding window.
       Here's how to find the character to be removed:
       Because the values in d represents the rightmost location of each character in the sliding window,
       in order to find the longest substring T, we need to locate the smallest location, and remove it from the dictionary, and then record the return value.
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Use dictionary d to keep track of (character, location) pair,
        # where location is the rightmost location that the character appears at
        d = {}
        low, ret = 0, 0
        for i, c in enumerate(s):
            # print ("i: "+ str(i) + "-- c: "+str(c))
            d[c] = i
            # print (d)
            if len(d) > k:
                low = min(d.values())
                # print("low: "+str(low))
                # print("d[s[low]]: "+str(d[s[low]]))
                del d[s[low]] #大于k的substring不需要
                low += 1 #从去掉的character的最右位的右边开始作为新的substring最左
            ret = max(i - low + 1, ret)   #i-low+1， 即当前substring最右-当前最左+1， 得当前substring 的长度
            # print (ret)
        return ret
```

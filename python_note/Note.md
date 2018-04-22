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


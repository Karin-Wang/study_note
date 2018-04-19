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

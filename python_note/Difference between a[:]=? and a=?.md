Using nums[:] will not allocate new memory, instead will change the values already used by nums. rather than just reassigning the name nums to the newly created list.

```
a = [1,2,3,4,5]
b = a
>> [1,2,3,4,5]
a[:] = [1, 2, 3]
print b 
>> [1, 2, 3]
```

b = a means set b to point to the memory location of a, then using [:] (slice of entire list) it modifies what b points to.

Using `OrderedDict` is a workaround to not having set() implemented.

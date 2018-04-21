# Map

## Use
```
map(function_to_apply, list_of_inputs)
```

## Example
```
>>> def f(x):
...     return x * x
...
>>> map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
[1, 4, 9, 16, 25, 36, 49, 64, 81]
```



# Reduce

## Use
```
reduce (func, seq[, init()]) 
```
Reduce is a really useful function for performing some computation on a list and returning the result. It applies a rolling computation to sequential pairs of values in a list. For example, if you wanted to compute the product of a list of integers.

## Example 1:

**Calcultate n!**

- no init(): The function will take 1 and 2 as x and y and then use its result to * 3
```
>>> n = 6
>>> print reduce(lambda x, y: x * y, range(1, n))
120
```

- with init(): The function will take 2 as init and let 2*1, then use the resukt to * 2
```
>>> print reduce(lambda x, y: x * y, range(1, n),2)
240
```

## Example 2:
```
from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])

# Output: 24

#The above code is equivalent to below
product = 1
list = [1, 2, 3, 4]
for num in list:
    product = product * num

# product = 24
```

# Filter

## Use

As the name suggests, filter creates a list of elements for which a function returns true. Here is a short and concise example:

## Example
```
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

# Output: [-5, -4, -3, -2, -1]
```

The filter resembles a for loop but it is a builtin function and faster.



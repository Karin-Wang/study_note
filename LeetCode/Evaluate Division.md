# Problem
Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given `a / b = 2.0`, `b / c = 3.0`. 

queries are: `a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? `. 

return `[6.0, 0.5, -1.0, 1.0, -1.0 ]`.

The input is: `vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>>` queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.`

According to the example above:

```
equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
```
The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.


# Soloution

Variation of Floyd-Warshall. Turn all the division result into a directed Graph, where the edges are the result of each division, like
`a/b = 2.0` => `a -> b = 2.0` and `b -> a = 1/2.0`

In addition, `a/d` can be represent as `(a/b)*(b/c)*(c/d)`, which is the path `a -> b -> c -> d`

```
class Solution(object):
    # variation of Floyd-Warshall
    def calcEquation(self, equations, values, queries):
        edge = collections.defaultdict(dict)
        for (num, den), val in zip(equations, values):
            edge[num][num] = edge[den][den] = 1.0
            edge[num][den] = val
            edge[den][num] = 1 / val
        for k, i, j in itertools.permutations(edge, 3):
            if k in edge[i] and j in edge[k]:
                edge[i][j] = edge[i][k] * edge[k][j]
                print("i: %s -- k : %s -- j : %s -- edge[i][j] = %d") %(i,k,j, edge[i][j])
        return [edge[num].get(den, -1.0) for num, den in queries]
```


###Note:
- collections.defaultdict(dict) is better than {}
- `dict.get(key, default=None)` here use `-1.0` as default 

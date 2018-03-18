# Course Schedule

## Problem

There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.


## Idea

Use Topological sort to detect if there is a closed loop inside the directed graph. If threr is a loop then it's not possible. 

Note that it's different from 


```
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        Indegrees = [0 for i in range(numCourses)]
        connections = {i:[] for i in range(numCourses)}
        for p in prerequisites:
            connections[p[1]].append(p[0])
            Indegrees[p[0]] += 1
        zero_Indegree = [i for i, x in enumerate(Indegrees) if x == 0]
        print (zero_Indegree)
        count = 0
        while (len(zero_Indegree)>0):
            count += 1
            for node in connections[zero_Indegree.pop()]:
                Indegrees[node] -= 1
                if Indegrees[node] == 0:
                    zero_Indegree.append(node)
        return (count == numCourses)



```

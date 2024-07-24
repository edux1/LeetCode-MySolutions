from collections import deque

class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        stack, paths = deque(), []
        for i in range(len(graph[0])):
            stack.append([0, graph[0][i]])
        
        while len(stack) > 0:
            path = stack.pop()
            print("path: {}".format(path))
            print("path[-1]: {}".format(path[-1]))
            if len(graph[path[-1]]) == 0:
                paths.append(path)
            
            for i in range(len(graph[path[-1]])):
                #print(" > {}".format(graph[path[-1]][i]))
                extended_path = list(path)

                extended_path.append(graph[path[-1]][i])
                stack.append(extended_path)

        return paths
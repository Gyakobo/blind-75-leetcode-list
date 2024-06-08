class Solution:
    def course_schedule(self, n, courses):
        # Create a dependency graph
        graph = {int:list}
        
        for c in courses:
            if c[0] not in graph:
                graph[c[0]] = [ c[1] ]
            else:
                graph[c[0]].append(c[1])



        # visited = set()

        print(graph)
 
n = 5 
courses = [ [0, 1], [0, 2], [1, 3], [1, 4], [3, 4] ]
s = Solution()
print(s.course_schedule(n, courses)) 


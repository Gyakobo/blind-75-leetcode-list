class Solution:
    def course_schedule(self, courses):
        # Create a dependency graph
        graph = { i[0]:i[1] for i in courses }

        passed = set()

        def dfs(c):
            if c in passed:
                return False

            

        print(graph)

courses = [ [4, 5], [3, 4], [2, 3], [1, 2], [0, 1] ]
s = Solution()
print(s.course_schedule(courses)) 


# https://leetcode.com/problems/course-schedule-iii/discuss/1187509/Python-Greedy-dp-with-proof-explained

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        heap, time = [], 0
        for t, end in sorted(courses, key=lambda x: x[1]):
            time += t
            heapq.heappush(heap, -t)
            if time > end:
                time += heapq.heappop(heap)
        return len(heap)
# -------------------------------------------------------------------
        # course = []
        # for i in sorted(courses, key = lambda x:x[1]):
        #     course.append(i[0])
        #     while sum(course) > i[1]:
        #         course.remove(max(course))
        # return len(course)
        
        